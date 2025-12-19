# Copyright Team Hector TU Darmstadt 2025
""" Wrapper module for substitution to resolve them once and cache the result."""

from launch.substitution import Substitution

class UniqueSubstitution(Substitution):
    """Container which ensures that the substitution produces a unique result 
    each time it is performed. Instead of the result changing."""

    def __init__(self, substitution: Substitution) -> None:
        """Create a UniqueSubstitution substitution."""
        super().__init__()
        self.substitution = substitution
        self.cached = {}

    def perform(self, context) -> str:
        """Perform the substitution by generating a unique string."""
        if not context in self.cached.keys():
            self.cached[context] = self.substitution.perform(context)
        return self.cached[context]