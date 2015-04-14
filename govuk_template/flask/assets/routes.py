from flask import send_from_directory


def register_routes(blueprint):
    @blueprint.route('/assets/<path:path>')
    def serve_assets(path):
        return send_from_directory('assets', path)
