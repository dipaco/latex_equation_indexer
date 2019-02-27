import os
import click
from constants import *
import models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


@click.group()
def main():
    pass


@click.command()
@click.argument('title')
@click.argument('math_text')
def add(title, math_text):

    session = models.create_or_get_data_base()

    # Insert a Person in the person table
    new_formula = models.MathText(title=title, latex_text=math_text)
    session.add(new_formula)
    session.commit()


@click.command()
def rm():
    click.echo('remove')


@click.command()
def search():
    session = models.create_or_get_data_base()
    query_results = session.query(models.MathText).all()
    #session.query(models.MathText).filter(models.MathText.title == 'titulo').all()

    for el in query_results:
        print('|------------------------------|')
        print('id: {}\t'.format(el.id))
        print('title: {}\t'.format(el.title))
        print('formula: {}\t'.format(el.latex_text))
        print('description: {}\t'.format(el.desc))
        print('bib_tex: {}\t'.format(el.bib_tex))
        print('|------------------------------|\n')


@click.command()
def gui():
    click.echo('gui')


main.add_command(add)
main.add_command(rm)
main.add_command(search)
main.add_command(search)
main.add_command(gui)

if __name__ == '__main__':

    main()
