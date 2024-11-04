class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, lice, aut):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.lice = lice
        self.aut = aut

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.lice} \n"

            f"\nAuthors: {self._stringify_dependencies(self.aut)}\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
