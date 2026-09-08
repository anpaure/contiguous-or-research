# Fixed actual19 embedded corrected21 connector diagnostic

Executed once on 2026-09-09, on h100 (hostname arboghast), after parent and
independent structure-agent full source/plan review. No retry or alternative
input, parent, cut, rotation, history, or matching was executed.

Remote directory:
`/home/amodo/exact-b-actual19-embedded-corrected21-connector-ages-20260909/`.

The exact shell command is preserved in [exact_command.txt](exact_command.txt).
Exit code: 0. Internal hard limits: 30 CPU seconds, 45 wall seconds,
1 GiB address space, 128 MiB per file. External wall guard: timeout45s.
Actual reported CPU: 0.542291545 seconds.
Actual reported wall time: 0.5424529858864844 seconds.

Source SHA-256:
`27388f115066d5f6270a8d8957bc3503d81ddf231aa5e65d989afeef0663a6dd`.
Input SHA-256:
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
Both pins were verified remotely before execution, and the checker itself
requires the raw-input pin. Source and input snapshots accompany the output.

Final report SHA-256:
`fe798b2a6dbc55c4307ed252f91ca4b53c02b88dd442e3c10d8eba90360aeecc`.
Complete bad-port list SHA-256:
`d177285f9e8fad4f6db5e45cb9a0b82cec6775b65f6303c143304a1add11f151`.

Observed outcome: 1,430 fixed ports, 1,371 good connectors, 59 bad age-one
ports. Every bad predecessor is exactly10D0. All explicit checks passed.
PASS denotes completion of this fixed diagnostic; it does not assert a
zero bad count or a spanning child construction.

All ten files listed in the remote-generated [SHA256SUMS](SHA256SUMS)
were copied locally and passed `shasum -a 256 -c SHA256SUMS`. This provenance
file and exact-command file were then added locally; no mathematical
computation was run during copying or hash verification.
