"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Ceva.

Configures offline-safe local intersphinx inventories across the GEOMETOR canon
(``euclid``, ``elements``, ``etc``, ``pappus``, ``ptolemy``, ``menelaus``,
``archimedes``, ``apollonius``, ``casey``, ``divine``, ``altshiller-court``,
``wildberger``, ``aquinas``, ``hoenen``, ``hilbert``, ``proclus``) and drops
unreachable remote-only targets so offline sandbox builds complete with zero warnings.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

SISTER_REPOS: tuple[str, ...] = (
    "euclid",
    "elements",
    "etc",
    "pappus",
    "ptolemy",
    "menelaus",
    "archimedes",
    "apollonius",
    "casey",
    "divine",
    "altshiller-court",
    "wildberger",
    "aquinas",
    "hoenen",
    "hilbert",
    "proclus",
)


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any],
    project_root: Path,
) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR repositories.

    Args:
        intersphinx_mapping: Mutable Sphinx ``intersphinx_mapping`` dictionary.
        project_root: Root directory of the ``ceva`` repository.
    """
    geometor_dir = project_root.parent
    for sister in SISTER_REPOS:
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    # Remove remote-only inventories lacking a local file so offline builds emit zero warnings
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: object) -> dict[str, object]:
    """Register the ``geometor.ceva.sphinx_ext`` Sphinx extension.

    Args:
        app: Active Sphinx application instance.

    Returns:
        Extension metadata dictionary.
    """
    del app
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
