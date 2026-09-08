# Independent audit: K17 OPTIMAL-28 static-shadow provider obstruction

## Outcome

The independent replay **reproduced** the claimed counts:

| provider envelope | targets | fixed distinct | possible distinct | zero support | meaning |
|---|---:|---:|---:|---:|---|
| upper q1 | 19448 | 14729 | 19230 | **218** | decisive fixed-skeleton no-go |
| lower q2, width 3 only | 19448 | 15551 | 19283 | **165** | canonical three-owner windows only |

Thus the saved ordered macro/packet skeleton cannot be completed to an
upper-q1-complete owner word by any residual pure-`U` port-pair assignment.
The 165 lower targets have no canonical width-three provider, but this does
**not** exclude their occurrence as intersections of longer intervals.

## Exhaustive reconstruction

The owner partition is literal: all 24310 rank-nine masks split into
19305 macro owners and 5005 pure-`U` owners.  The
packet path fixes 133 pure-`U` objects and leaves
4872 residual ones.  The 6435 old rank-eight ports have
demand profile `{0: 691, 1: 1744, 2: 4000}`.

Every upper adjacent pair is exactly one of:

1. an internal macro pair;
2. a saturated fixed port junction (`M-M`, `M-U`, or `U-U`);
3. a demand-one fixed-endpoint/residual-`U` junction; or
4. a demand-two residual-`U`/residual-`U` junction.

The concrete demand-one endpoint profile is
`{'M': 1744}`: the generic pure-`U`
endpoint branch is retained by the verifier and has zero instances here.

| upper provider family | locally admissible events | distinct targets |
|---|---:|---:|
| macro internal (fixed) | 17875 | 14658 |
| saturated `M-M` (fixed) | 441 | 441 |
| saturated `M-U` (fixed) | 234 | 180 |
| saturated `U-U` (fixed) | 16 | 16 |
| demand-one `M-R` | 11952 | 7150 |
| demand-one `U-R` | 0 | 0 |
| demand-two `R-R` | 80449 | 3003 |

Every canonical width-three lower window is classified by its central owner:
an internal/endpoint macro owner, a fixed singleton `U`, or a residual
singleton `U`.  In the last case its value is exactly `p & q` for the chosen
positive-demand facets `p,q`.

| width-three lower provider family | candidate events | distinct targets |
|---|---:|---:|
| macro internal centre (fixed) | 16445 | 13287 |
| macro endpoint centre (fixed) | 2860 | 2417 |
| fixed-`U` centre | 133 | 133 |
| residual-`U` centre, `p & q` | 141255 | 6435 |

## Why the upper count is decisive

Consecutive owners are distinct rank-nine Johnson neighbours, so their union
has rank ten.  If an interval has rank-ten union `H`, every adjacent pair in
that interval has a rank-ten union contained in `H`, hence equal to `H`.
Therefore every rank-ten interval target has an adjacent-pair witness.  The
218 targets absent even from the local
adjacent-pair envelope are impossible for every globally feasible residual
assignment.

## Exact scope and nonclaims

The positive-provider catalogue is local: it deliberately does not prove that
each candidate extends to a simultaneous residual b-flow, one cycle, or a
residence/common-cap-compatible completion.  This only strengthens the zero
support conclusion, because the enumerated set is a superset of providers in
any actual assignment.  The audit preserves the ordered macro-to-port
incidences and fixed packet selection.  It says nothing about macro
reorientation/splitting, packet reselection, complementary residence, upper
q2/q3, or common-cap Hall.

For the lower side, the central-owner classification exhausts width three but
not longer intervals.  A longer intersection may drop to rank seven only after
more than three owners, so the 165 count is
not a global lower-shadow obstruction.

## Frozen artifacts

- Script: `scratch/h3_independent_audit_ad_k17_opt28_static_shadow_provider_no_go_20260731.py` — SHA-256 `44b5e84186685e91230d8df8bd6761991367bbd0973c751e563fe1a76a9ad5e4`
- JSON: `scratch/h3_ad_k17_opt28_static_shadow_provider_no_go_20260731.audit.json` — SHA-256 `c1c31f76b39cb65c621c720cc19f0748a268e2be2ee5cb137227dfb19bae8949`
- JSON payload SHA-256: `1a45c98a24c14c3ccd1aea805a9459ff420736a9b27d3dddd607b1508b8edb38`
- Subject script audited: SHA-256 `1f3462406f157861af8a549904540608320c9e1df0a6ec9f84994172804f9503`
- Subject JSON snapshot audited: SHA-256 `cb10e939bcdb1e73f08f0cca0b6318c52487acd283a49c63be821c9488d2f857`
- Subject payload valid at snapshot: `True`

The JSON freezes the complete decimal and hexadecimal lists of all
218 upper and
165 width-three lower zero-support targets,
plus per-family event/distinct-target counts and all primary input hashes.
