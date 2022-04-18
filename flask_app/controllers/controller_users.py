from flask import render_template, request, redirect, session
from flask_app import app


from flask_app.models.model_user import User


@app.route('/users/new')
def create():
    create_all_user = User.get_all()
    return render_template("create.html", all_users=create_all_user)


@app.route('/users')
def result():
    create_all_user = User.get_all()
    return render_template("result.html", all_users=create_all_user)


@app.route('/user/<int:id>')
def readone(id):
    user_data = {"id": id}
    just_user = User.get_one(user_data)
    return render_template("readone.html", one_user=just_user)


@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    create_one_user = User.get_one(data)
    return render_template("edit.html", user=create_one_user)


@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")


@app.route('/user/create', methods=['post'])
def goreadone():
    # print(request.form)
    user_id = User.create(request.form)
    return redirect(f"/user/{user_id}")


@app.route('/user/<int:id>/update', methods=['POST'])
def update(id):
    data = {
        **request.form, "id": id
    }
    User.update_one(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)


# ****************************
