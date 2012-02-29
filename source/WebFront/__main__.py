'''
Created on Feb 28, 2012

@author: leanother
'''
import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

from Zukofsky import zukofsky

cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 8080,
                        'tools.sessions.on' : True,
                        'tools.sessions.storage_type' : "file",
                        'tools.sessions.storage_path' : "/home/leanother/sessions",
                        'tools.sessions.timeout' : 60,
                       })

class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(version=zukofsky.get_version(),
                            auth_url=zukofsky.get_url())
    @cherrypy.expose
    def menu(self,verifier=None):
        tmpl = env.get_template('menu.html')
        if cherrypy.session.get('api') != None:
            pass
        else:
            cherrypy.session['api'] = zukofsky.get_api(verifier)
            api = cherrypy.session['api']
            cherrypy.session['friends'] = zukofsky.get_friends(api)
            cherrypy.session['followers'] = zukofsky.get_followers(api)
        return tmpl.render(friends=cherrypy.session.get('friends'),
                            followers=cherrypy.session.get('followers'))
    @cherrypy.expose    
    def theynot(self):
        tmpl = env.get_template('theynot.html')
        friendsnot = []
        for friend in cherrypy.session.get('friends'):
            if cherrypy.session.get('followers').count(friend) == 0:
                friendsnot.append(friend)
        return tmpl.render(friends=friendsnot)
    
    @cherrypy.expose
    def younot(self):
        tmpl = env.get_template('younot.html')
        followersnot = []
        for follower in cherrypy.session.get('followers'):
            if cherrypy.session.get('friends').count(follower) == 0:
                followersnot.append(follower)
        return tmpl.render(followers=followersnot)
    
    @cherrypy.expose()
    def blocked(self):
        tmpl = env.get_template('blocked.html')
        return tmpl.render(blocks = cherrypy.session['api'].blocks())
    
    @cherrypy.expose
    def expire(self):
        cherrypy.lib.sessions.expire()
        return "Expire!"
      
if __name__ == '__main__':
    cherrypy.quickstart(Root())
