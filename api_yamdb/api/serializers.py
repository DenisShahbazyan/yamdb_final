from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Category, Comments, Genre, Review, Title
from users.models import CHOICES_ROLE, User

from api_yamdb.settings import MIN_LEN_USERNAME, THIS_YEAR


class CreateUserSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if len(value) <= MIN_LEN_USERNAME:
            raise serializers.ValidationError(
                'Поле username должно быть более 2х символов')
        return value

    class Meta:
        model = User
        fields = ('email', 'username')


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=25,
        required=True
    )
    confirmation_code = serializers.CharField(
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(
        choices=CHOICES_ROLE,
        required=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class CurrentTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return get_object_or_404(
            Title, id=serializer_field.context['title_id'])


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    title = serializers.HiddenField(default=CurrentTitleDefault())

    def validate_score(self, value):
        if not (1 <= value <= 10):
            raise serializers.ValidationError(
                'Некорректное значение рейтинга. '
                'Пожалуйста задайте от 1 до 10.')
        return value

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('title',)

        validators = (
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title', 'author'),
                message=("Можно оставить только один отзыв на произведение.")
            ),
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comments
        exclude = ('review', )
        read_only_fields = ('review',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', 'slug']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True, default=None)
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = [
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category',
        ]

    def validate_year(self, value):
        if not (0 < value <= THIS_YEAR):
            raise serializers.ValidationError(
                f'Год должен быть больше 0 и меньше {THIS_YEAR}!'
            )
        return value


class TitleSerializerGet(TitleSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
