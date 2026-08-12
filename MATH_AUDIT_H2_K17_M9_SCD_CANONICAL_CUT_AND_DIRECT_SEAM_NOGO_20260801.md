# The authenticated `m=9` SCD forest: exact residence cuts and a direct-seam obstruction

Date: 2026-08-01  
Lane: H2 independent finite `k=17` replay  
Status: exact source-relative audit; canonical minimum-cut/direct-endpoint-braid
no-go.  No unrestricted `k=17` no-go.

## 1. Scope and verdict

The authenticated selected-option catalogue

`scratch/h2_k17_m9_multicomponent_20260801/phase_m9.selected.tsv`

has SHA

`49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de`.

An independent reconstruction of the four-row SCD matching and every
untouched provider gives exactly

\[
 24310\text{ rank-nine owners},\qquad
 19448\text{ directed edges},\qquad
 4862\text{ path components}.
\]

The intact-component proposal fails: 1,213 components are not depth-three
factorable.  Cutting each short internal positive run by the canonical
right-end interval transversal needs exactly 1,419 cuts and produces 6,281
factorable pieces.  The cuts delete 1,419 pairwise-distinct rank-ten edge
colours.

This canonical cut face still cannot be completed by orienting the pieces
and putting one direct Johnson edge at every join.  Two pieces have no
locally factorable incoming or outgoing direct seam in either orientation.
Moreover 322 of the 1,419 deleted rank-ten colours cannot occur on any
locally factorable direct seam between piece endpoints.

The conclusion is deliberately narrow.  It does not cover a different
minimum transversal, extra cuts, a multi-owner seam circuit, an interior
rethread, or a generalized source/compiler construction not represented by
one endpoint Johnson edge per join.

## 2. Exact intact-component failure

For an owner path

\[
 O_0,O_1,\ldots,O_t
\]

at depth three, its maximal source letters are

\[
 E_p=\bigcap_{\max(0,p-3)\le i\le\min(t,p)}O_i.
\]

The equality `D^3 E=O` holds iff every internal positive coordinate run in
the owner trace has length at least four.  All maximal letters in the frozen
forest are nonempty, so this run condition is the only failure.

The exact census is

| test | bad components | bad internal runs |
|---|---:|---:|
| length below 3 | 914 | 1,076 |
| length below 4 | 1,213 | 1,736 |

Thus only 3,649 of the 4,862 intact components are depth-three factorable.
The smallest displayed obstruction is component 5:

\[
 (1855,895,65919,98623).
\]

Coordinate `0x40` has trace `0110`.  It occurs in the two internal owners
but in no maximal depth-three source position, so owner rows 1 and 2 both
lose `0x40`.  Reversing or externally ordering the component does not alter
this internal obstruction.

There is an independent terminal-socket loss.  After imposing every owner,
internal lower-q1 row, and the directed sink lower socket, only 3,292
components have a common source.  Of the 3,649 factorable components, 357
fail solely at the terminal socket.  On a factorable component with sink
root `L_t` and terminal owner `M_0(L_t)=L_t+x`, the exact local condition is

\[
 x\in\bigcap_{j=\max(0,t-3)}^t O_j.                 \tag{2.1}
\]

The first terminal-only failure is component 37: its terminal extra
coordinate is bit 6, while the last-four-owner intersection is 67635 and
omits that bit.

## 3. Canonical minimum cuts

An internal positive run on owner indices `[l,r]`, of length below four,
becomes boundary-clipped exactly when a cut position in

\[
 [l,r+1]
\]

is selected.  Hence the minimum-cut problem on each component is ordinary
interval stabbing.  Sort the intervals by right endpoint and select the
right endpoint of the first unhit interval.  The selected intervals are
pairwise disjoint in cut-position space, so their number is simultaneously
a packing lower bound.  This proves optimality component by component.

The resulting ledger is

| cuts in a component | number of components |
|---:|---:|
| 0 | 3,649 |
| 1 | 1,037 |
| 2 | 149 |
| 3 | 24 |
| 4 | 3 |

Thus

\[
 1419\text{ cuts},\qquad 6281\text{ pieces},\qquad
 18029\text{ preserved edges}.                    \tag{3.1}
\]

Every removed lower edge label and every removed upper edge label is
distinct.  The missing lower-q1 bank consists of the 4,862 old component
sinks and the 1,419 cut labels, disjointly, hence has size 6,281.

### Residence terminology

Equation (3.1) makes the **owner row** depth-three factorable.  If one also
requires the maximal source `E` itself to have every internal positive run
of length at least four, an internal owner run must have length at least
seven because maximal erosion shortens it by three.  Applying the same
minimum interval argument at threshold seven gives

\[
 1634\text{ cuts},\qquad6496\text{ pieces},          \tag{3.2}
\]

and only 3,504 intact components pass.  The 1,419- and 1,634-cut faces must
not be conflated.

## 4. Exact post-cut upper deck

For every original component and every `q=1,...,5`, the audit enumerates all
`q`-edge paths, keeps only unions of rank `9+q`, and removes precisely those
path addresses crossing a canonical cut.  The result is:

| rank | original holes | new cut casualties | post-cut holes |
|---:|---:|---:|---:|
| 10 | 0 | 1,419 | 1,419 |
| 11 | 911 | 1,543 | 2,454 |
| 12 | 608 | 1,047 | 1,655 |
| 13 | 172 | 482 | 654 |
| 14 | 26 | 144 | 170 |

At rank ten the 1,419 crossing addresses give 1,419 distinct values with
no duplicate and no alternate witness.  At higher rank alternate witnesses
and repeated crossing values are replayed explicitly in the JSON audit.
Consequently every cut rank-ten colour must be supplied by the eventual
seam/rethread system.

## 5. Oriented boundary state and direct-seam no-go

Each of the 6,281 pieces is stored in both orientations, except that a
singleton has only one state.  This gives 12,202 oriented states.  A state
contains:

1. for each of the 17 coordinates, the signed first/last values, exact
   prefix/suffix run ages, and the all-constant flag;
2. prefix and suffix unions of its rank-ten edge labels through width five;
3. prefix and suffix unions of its maximal source through depth three; and
4. its first and last three literal maximal-source letters.

These are sufficient to replay the local factorability of a direct Johnson
seam and every crossing upper path through rank fourteen.  They are boundary
state, not a proof that one common cap exists.

The exact endpoint census is

| row | count |
|---|---:|
| oriented endpoint Johnson candidates | 493,910 |
| locally depth-three-factorable seams | 118,534 |
| locally factorable seams whose lower label is in the missing bank | 64,416 |

Already before imposing lower-label uniqueness, pieces 1203 and 2332 have
no locally factorable incoming or outgoing seam in either orientation:

\[
\begin{aligned}
1203 &: (28370,77522,108242),\\
2332 &: (24236,28332,77484,108204).
\end{aligned}
\]

A directed spanning path permits only one source and one sink; an isolated
piece cannot occur in it.  Hence the direct endpoint braid is impossible.

There is a separate colour obstruction.  Only 1,097 of the 1,419 deleted
rank-ten colours occur on any locally factorable endpoint seam, leaving 322
unsupported.  The first is `0x03ff=1023`.  It came from component 112,
cut position 4,

\[
 991\longrightarrow511,qquad
 991\cup511=1023,qquad991\cap511=479,
\]

where bit 9 has the private internal run of length two.  No other oriented
piece-end pair supplies upper colour 1023 while passing the local depth-three
test.

Restoring any one of the 1,419 original cut edges is also locally illegal:
the disjoint-interval packing gives that cut a private short run, which
becomes internal again upon restoration.

## 6. Exact surviving gate

The canonical minimum-cut, one-direct-Johnson-edge-per-join face is closed.
An escape must change at least one of its defining choices:

* choose a different simultaneous cut transversal;
* add cuts and thereby expose new endpoints;
* use a multi-owner incidence circuit or interior rethread at a seam; or
* abandon the direct owner braid in favour of a more general source/compiler
  construction.

Any such escape must still redeliver the complete 1,419-colour rank-ten cut
bank, repair the displayed rank-11--14 holes, carry the signed run-age state,
and satisfy all target occurrences under one maximal common cap.  The scalar
length slack alone proves none of these rows.

## 7. Audit artifacts

* `scratch/audit_h2_k17_m9_scd_component_factorability_20260801.py`
* `scratch/h2_k17_m9_multicomponent_20260801/component_factorability.audit.json`
* `scratch/audit_h2_k17_m9_scd_canonical_cut_and_seams_20260801.py`
* `scratch/h2_k17_m9_multicomponent_20260801/canonical_cut_and_seams.audit.json`
* `scratch/h2_k17_m9_multicomponent_20260801/canonical_factor_cuts.tsv`
* `scratch/h2_k17_m9_multicomponent_20260801/oriented_piece_states.tsv`
* `scratch/h2_k17_m9_multicomponent_20260801/legal_seam_catalogue.tsv`

