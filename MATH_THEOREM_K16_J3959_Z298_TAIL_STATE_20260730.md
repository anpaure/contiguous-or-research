# The Z298 tail-state obstruction for signed j3959 component moves

Fix collar 5960 and let `Z` be the authenticated set of 298 zero-degree
lower targets of c5960.  In the j3959 source, `Z` has 317 distinct physical
provider cells.  Exactly 305 lie wholly in the two-flat tail component `I8`:
304 have length two and one has length one.  For 288 targets every source
provider lies in `I8`.

## Dependency-closed state catalogue

A component cell is *deep* when its complete profile-dependency interval is
internal.  At entry phase `p` this interval is conservatively and exactly
contained in `[cell_start-2p,cell_stop+p)`: envelopes depend on preceding
scheduled rows, and mandatory carriers add one further envelope radius.  Its
envelopes, mandatory carriers, and provider signature then depend only on
the oriented component and its entry phase.

Exact allowed-submask enumeration gives zero deep `Z`-providers for every
orientation and legal entry phase of `I0,...,I7`.  For `I8` the complete
catalogue is:

| state | exit phase | deep provider cells | covered Z targets |
|---|---:|---:|---:|
| `F@2` | 0 | 303 | 286 |
| `F@3` | 1 | 192 | 180 |
| `R@2` | 0 | 0 | 0 |
| `R@3` | 1 | 301 | 286 |

Thus `R@3` is a genuine escape and no unconditional theorem can force
forward orientation.  At entry phase two, however, reversal destroys every
dependency-closed provider.

## Rigorous exception capacity

Charge every non-deep cell to a piece seam crossed by its profile-dependency
interval.  Direct interval counting gives exactly 30 possibly affected cells
at a phase-three seam and 13 at a phase-two seam.  The phase-two collar has
zero deep `Z` providers by exact enumeration.  If `r<=7` zero-flat components
precede the one-flat component, at most `r` ordinary seams are phase three
and `8-r` are phase two.  Charging the special seam into `I8=R@2`
conservatively at 30 gives

`30r + 13(8-r) + 30 = 134+17r <= 253`.

This seam charge includes internal halos, crossing cells, and collar
dependencies without double reliance on an incomplete three-row halo.
If `I8=R@2`, and `C` additional right vertices outside this frozen
class are admitted by a wider move, Hall applied to `Z` gives

`deficiency >= 298-(253+C)=45-C`.

Consequently, if a wider class promises full Hall deficiency at most
`25+C`, then `R@2` is impossible whenever `C<=9`.  In the fixed search
normal form where the collar starts at depth two and `I8` follows it carrying
the remaining two flats, `I8` necessarily enters at phase two; under the
same bound it must therefore be forward.

This is the strongest orientation conclusion supported by the catalogue.
It does not exclude `R@3`, and the capacity 253 is deliberately an
overcount, so no smaller exception bound is claimed without further seam
signature analysis.  The theorem is source-relative and makes no global K16
claim.
