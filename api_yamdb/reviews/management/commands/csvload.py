from django.core.management.base import BaseCommand
from reviews.models import Category, Comments, Genre, Review, Title
from reviews.parsers.csv_parsers import csv_parse
from users.models import User


def create_category(fields_list):
    for fields in fields_list:
        Category.objects.get_or_create(
            name=fields['name'],
            slug=fields['slug'],
        )


def create_genre(fields_list):
    for fields in fields_list:
        Genre.objects.get_or_create(
            name=fields['name'],
            slug=fields['slug'],
        )


def create_titles(fields_list):
    for fields in fields_list:
        category = Category.objects.filter(pk=fields['category']).first()
        Title.objects.get_or_create(
            name=fields['name'],
            year=fields['year'],
            category=category,
        )


def create_review(fields_list):
    for fields in fields_list:
        title = Title.objects.filter(pk=fields['title_id']).first()
        author = User.objects.filter(pk=fields['author']).first()
        Review.objects.get_or_create(
            text=fields['text'],
            score=fields['score'],
            title=title,
            pub_date=fields['pub_date'],
            author=author,
        )


def create_comments(fields_list):
    for fields in fields_list:
        review = Review.objects.filter(pk=fields['review_id']).first()
        Comments.objects.get_or_create(
            text=fields['text'],
            pub_date=fields['pub_date'],
            review=review,
        )


def create_users(fields_list):
    for fields in fields_list:
        User.objects.get_or_create(
            id=fields['id'],
            username=fields['username'],
            email=fields['email'],
            role=fields['role'],
            bio=fields['bio'],
            first_name=fields['first_name'],
            last_name=fields['last_name'],
        )


def create_genre_title(fields_list):
    for fields in fields_list:
        title = Title.objects.filter(pk=fields['title_id']).first()
        genre = Genre.objects.filter(pk=fields['genre_id']).first()
        title.genre.add(genre)


class Command(BaseCommand):
    '''Load data from csv file.'''

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        filename = options['filename']
        fields_list = csv_parse(filename)
        if not fields_list:
            self.stdout.write(self.style.ERROR(
                f'file {filename}.csv not exist'
            ))

        commands = {
            'category': create_category,
            'genre': create_genre,
            'titles': create_titles,
            'review': create_review,
            'comments': create_comments,
            'users': create_users,
            'genre_title': create_genre_title,
        }

        try:
            commands.get(filename)(fields_list)
            self.stdout.write(self.style.SUCCESS(
                f'Data in "{filename}" table is created.'))
        except TypeError:
            self.stdout.write(self.style.ERROR(
                f'Table {filename} is not exist'))
