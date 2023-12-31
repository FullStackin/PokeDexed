"""empty message

Revision ID: 6661981da970
Revises: 
Create Date: 2023-06-29 13:25:48.256543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6661981da970'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Pokemons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('imageUrl', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.Enum('fire', 'electric', 'normal', 'ghost', 'psychic', 'water', 'bug', 'dragon', 'grass', 'fighting', 'ice', 'flying', 'poison', 'ground', 'rock', 'steel', name='pokemontypes'), nullable=False),
    sa.Column('moves', sa.String(length=255), nullable=False),
    sa.Column('encounterRate', sa.Float(precision=3, asdecimal=2), nullable=False),
    sa.Column('catchRate', sa.Float(precision=3, asdecimal=2), nullable=False),
    sa.Column('captured', sa.Boolean(), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('number')
    )
    op.create_table('Items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('happiness', sa.Integer(), nullable=False),
    sa.Column('imageUrl', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('pokemonId', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pokemonId'], ['Pokemons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Items')
    op.drop_table('Pokemons')
    # ### end Alembic commands ###
