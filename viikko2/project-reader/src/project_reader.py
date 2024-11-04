from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        par_toml = toml.loads(content)

        #print(par_toml)

        name = par_toml["tool"]["poetry"]["name"]

        des = par_toml["tool"]["poetry"]["description"]

        dep = [i for i in par_toml["tool"]["poetry"]["dependencies"]]

        ep = [ i for i in par_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]]

        lice = par_toml["tool"]["poetry"]["license"]

        aut = [i for i in par_toml["tool"]["poetry"]["authors"]]
        #new_toml = toml.dumps(par_toml)

        #print(new_toml)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, des , dep, ep, lice, aut)
