from flask import jsonify, request
from models import db, Book


def init_routes(app):
    @app.route('/')
    def home():
        return 'Welcome to the library!'

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = Book(
            title=data['title'],
            author=data.get('author'))
        db.session.add(new_book)
        db.session.commit()
        return jsonify({
            'message': 'Book added!',
            'id': new_book.id
        }), 201

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])

    @app.route('/books/<int:id>', methods=['PUT'])
    def update_book(id):
        book = Book.query.get_or_404(id)
        data = request.get_json()
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        db.session.commit()
        return jsonify({'message': 'The book has been updated.'})

    @app.route('/books/<int:id>', methods=['DELETE'])
    def delete_book(id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "The book has been deleted."}), 200