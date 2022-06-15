from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.congig.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    import HomePage, ProfilePage, ParkingLotPage, LoginPage, RegisterPage, AdministratorPage

    app.register_blueprint(HomePage.bp)
    app.register_blueprint(ProfilePage.bp)
    app.register_blueprint(ParkingLotPage.bp)
    app.register_blueprint(LoginPage.bp)
    app.register_blueprint(RegisterPage.bp)
    app.register_blueprint(AdministratorPage.bp)

    return app


