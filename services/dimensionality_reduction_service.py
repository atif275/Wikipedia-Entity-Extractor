from typing import Any, Sequence


class DimensionalityReductionService:
    def __init__(self, dimensionality_reducer: Any) -> None:
        self._dimensionality_reducer = dimensionality_reducer
        pass

    @property
    def dimensionality_reducer(self):
        return self._dimensionality_reducer

    def reduce_dimensions(
        self, higher_dimensional_input: Any
    ) -> Sequence[Sequence[float]]:
        return self.dimensionality_reducer.fit_transform(higher_dimensional_input)
