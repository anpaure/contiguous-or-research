#!/usr/bin/env python3
"""Canonical entry point for the rooted-conflict microbite audit.

The substantive checker lives beside this file under its original shorter name.
Keeping this entry point makes the theorem-note provenance literal while avoiding
two independently drifting copies of the same audit.
"""

from audit_rooted_conflict_exposure_microbite_20260822 import main


if __name__ == "__main__":
    main()
