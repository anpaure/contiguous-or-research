# Folded C8 aligned ray bases obey a sharp distance bound, but supply no native recyclable host

Date: 2026-08-01  
Lane: AD, folded quotient two-ray physicalization  
Status: all-`d` local flat/nonflat obstruction conditional on the displayed
aligned two-ray bases and traces; the folded common-cut census and numerical
formulas are independently audited for `5<=d<=12`.  An owner-rethreaded
exterior planting remains open.

## 0. Verdict and exact face separation

The folded owner quotient is a major reduction: its resident Hamilton paths
have only two directed source rays in each phase, totaling `2(d-1)` values.
The exact owner bank has a further rigid property: precisely one owner
contains both active labels `a1,a3`.  It follows that two interior one-sided
ray anchors in a simple flat depth-`d` chronology must be separated by at
least `d` source positions.  Both aligned faces below attain this bound.

The frozen upstream replay
`scratch/audit_c8_folded_hamilton_two_ray_lift_20260801.py` now passes and
separates three canonical faces: minimum signature, minimum aligned base,
and minimum upper-support-safe.  The first two retain only fifteen local
immediate-upper support labels, while the third has displaced ray addresses.
The present
audit searches the larger family in which the two displayed base values
may use any aligned singleton occurrences and additionally requires all
sixteen upper-support values.  In that distinct family the lexicographically
first minimum row gives

\[
  p=4d+10,\qquad q=5d+10,\qquad q-p=d,                 \tag{0.1}
\]

for the lexicographically first minimum aligned face, and its graded source
counter distance is

\[
                            22d+44.                      \tag{0.2}
\]

There are `4d+8` aligned ray-clean rows and `4d+4` aligned upper-support-safe
rows.  Other tied aligned rows translate both addresses, but retain
separation `d`.  The canonical aligned face is different: its anchors are
`4d+12,5d+12`, its graded distance is `10d+12`, and its cut retains only
fifteen upper-support values.

At (0.1), write

\[
\begin{aligned}
 P_0&=K\cup\{z,a_3,f_1\},&P_1&=K\cup\{z,a_1,f_1\},\\
 S_0&=K\cup\{z,a_1,f_d\},&S_1&=K\cup\{z,a_3,f_d\},
\end{aligned}                                           \tag{0.3}
\]

and

\[
 H_P=P_0\cup P_1,qquad H_S=S_0\cup S_1.               \tag{0.4}
\]

The two natural physical host realizations both fail as strict flat factor
moves, for different exact reasons.

1. Retaining the whole old host (`H_P,P_(1-epsilon)` on the prefix side and
   `S_(1-epsilon),H_S` on the suffix side) creates exactly two rank-`r+1`
   owner windows in each phase.
2. Pairing the two phase bases (`P_epsilon,P_(1-epsilon)` and
   `S_(1-epsilon),S_epsilon`) keeps every owner at rank `r` and remains
   resident, but forces three consecutive equal owners.  It changes the
   owner and lower-q1 multisets between phases, and its source decks still
   differ in exactly `8d-16` values each way.

Thus the two-ray reduction does not yet give two legal recyclable internal
split hosts.  It does reduce the remaining positive object to an
owner-rethreaded or exterior two-host insertion with a joint compiler Hall
certificate.  Neither face lies in the strict upper-rainbow selector: even
the sixteen-value face is only support-surjective and has the load
obstruction recorded in item `2415L`.

## 1. The two aligned folded faces

For each phase, the folded lower-rainbow degree-two system has 16 solutions,
all Hamilton cycles, and exactly two cover all sixteen immediate-upper
support labels.  Open one old and one new upper-support-surjective cycle at a
common edge and orient them with common endpoints.  Filter to pairs satisfying:

* no residence defect;
* the exact two-ray directed deck formula;
* all 16 upper-support values after the cut; and
* equal physical singleton positions for the two phase bases of each ray.

For every audited `5<=d<=12`, the exact counts are

\[
 \#\text{aligned}=4d+8,qquad
 \#\text{aligned and upper-support-safe}=4d+4.          \tag{1.1}
\]

The audited minimum graded discrepancy in this enlarged aligned-and-safe
family is (0.2).  One tied orientation has (0.1); reversal gives the
symmetric order.  This does not replace the canonical aligned face at
`4d+12,5d+12`: that face has graded distance `10d+12` and loses one upper
support value.  Both faces have anchor separation exactly `d`.  Nor does the
enlarged face make the folded path upper-rainbow; “all sixteen upper values”
here is support-surjectivity only.

The exact strict-upper counters make the distinction quantitative.  A
support-surjective cycle has load profile

\[
                           1^8(d+2)^8.                  \tag{1.2}
\]

After the canonical aligned cut the path profile is `1^7(d+2)^8`, so its
strict-upper partition rank/nullity are `15` and `8d+8`.  After an
upper-support-safe cut the profile is `1^8(d+1)^1(d+2)^7`, giving rank `16`
and nullity `8d+7`.  Therefore no residual selector can retain either whole
literal folded path in an upper-exact Catalan forest.  The host calculations
below are conditional source/support statements; they prove no strict-upper
host planting.

## 2. Unique mixed owner and the sharp distance-`d` bound

Let `V_d` be the `8d+24`-vertex folded owner bank.  The exact census gives

\[
 \#\{T\in V_d:\{a_1,a_3\}\subseteq T\}=1,             \tag{2.1}
\]

and its unique member is

\[
 U=K\cup\{z,a_1,a_3\}\cup F[1,d].                    \tag{2.2}
\]

Indeed, ordinary tensor owners have one active `C8` vertex, intersection
screens have active rank one, and the sole union screen with both nonadjacent
actives is `A1 union A3`; its four raw occurrences collapse to (2.2) in the
owner-value quotient.  Thus (2.1) is an all-`d` statement.  The replay checks
the resulting bank independently for `5<=d<=12`.

Now let `Q` be any depth-`d` source dilating to a simple owner word whose
owner set is `V_d`.  Suppose two **interior** source positions `p<q` contain
`a3` and `a1`, respectively.  Their incident owner-index intervals are

\[
 I(p)=[p-d,p],\qquad I(q)=[q-d,q].                     \tag{2.3}
\]

If `h=q-p<=d`, then

\[
                         |I(p)\cap I(q)|=d+1-h.        \tag{2.4}
\]

Every owner indexed by this intersection contains both active labels, hence
must equal `U` by (2.1).  Simplicity permits at most one such row.  Therefore

\[
                              q-p\ge d.                \tag{2.5}
\]

Equality is sharp: it leaves one common owner window, necessarily `U`, and
both aligned folded faces attain it.  Conversely, if the cross-host interval
must itself be an admissible depth-`d` cell, its length is `q-p+1<=d+1`, hence
`q-p<=d`.  Owner simplicity and deadline therefore force

\[
                              q-p=d.                   \tag{2.6}
\]

This is the exact two-anchor lower/equality bound.  It applies to one-sided
active bases.  A full internal host containing both active labels is stronger
still: all `d+1` incident owner windows would have to equal `U`, so no such
full host is native in a simple chronology.

## 3. Native host impossibility from maximal erosion

Let `T` be either chosen owner path and `E` its maximal depth-`d` erosion.
Every source `Q` which dilates to the same `T` satisfies

\[
 Q_j\subseteq E_j=\bigcap_{i:\,i\le j\le i+d}T_i.       \tag{3.1}
\]

At the two base addresses the maximal letters are precisely the three-label
sets in (0.3), while each desired host in (0.4) contains the opposite private
active label.  Hence

\[
                         H_P\nsubseteq E_p,qquad
                         H_S\nsubseteq E_q.              \tag{3.2}
\]

No unchanged folded owner path can contain either host as a native source
letter.  Planting them necessarily changes the owner chronology or moves the
hosts to an exterior occurrence.

## 4. Whole-host planting produces a rank ridge

The lossless split-letter normal form would retain the full host and expose
the opposite ray base.  In phase `epsilon` its two local blocks are

\[
              (H_P,P_{1-\epsilon}),qquad
              (S_{1-\epsilon},H_S).                     \tag{4.1}
\]

The two positions are separated by `d` in the contracted source.  Direct
evaluation of the `d+1`-letter owner windows shows that all but two retain
rank `r`, while two contain the extra private active label and have rank
`r+1`.  Thus the full-host form preserves the hypothetical contracted deck
but is not a flat owner word.

This is also immediate from (3.2): maximal erosion is the largest letter
compatible with the unchanged owner path, so adjoining the missing private
label must enlarge at least one incident owner.

## 5. Base-pair planting produces an exact stutter

One may avoid the rank ridge by omitting the full host and putting the two
phase bases themselves in opposite orders:

\[
 (P_0,P_1),\ (S_1,S_0)quad\longleftrightarrow\quad
 (P_1,P_0),\ (S_0,S_1).                                 \tag{5.1}
\]

Because `q-p=d`, the two insertions compensate the rank deficit of either
single split.  Every new depth-`d` owner window has rank exactly `r`.  The
complete active/filler union between the two bases is

\[
             U=K\cup\{z,a_1,a_3\}\cup F[1,d],          \tag{5.2}
\]

and the three owner windows beginning at `p,p+1,p+2` all equal `U`:

\[
                    \widetilde T_p=widetilde T_{p+1}
                                  =\widetilde T_{p+2}.   \tag{5.3}
\]

Thus (4.1) is a resident rank-`r` walk but not a strict Johnson path.  The
stutter is forced by the ray orientations; reversing one of the two blocks
destroys the corresponding one-sided ray.

The failure is not merely cosmetic.  For every audited `5<=d<=12`, the two phase
walks have different owner and lower-intersection multisets (their repeated
upper-union Counters still agree; this is not injectivity).  If
`SuppDeck(Q)` denotes the **set** of distinct interval-OR values of `Q`, then
the expanded sources satisfy

\[
 |SuppDeck(\widetilde Q^0)-SuppDeck(\widetilde Q^1)|
 =|SuppDeck(\widetilde Q^1)-SuppDeck(\widetilde Q^0)|=8d-16. \tag{5.4}

Some old same-phase interval values are also lost because (4.1) is not a
union-preserving refinement of `P_epsilon` or `S_epsilon`.  Hence treating
the stutters as two harmless extra positions does not close the compiler.

## 6. Exact remaining positive target

The folded quotient has genuinely reduced the old `8/9` interface to two
rays, but a positive theorem must change one more layer.  It may:

1. reroot/rethread the owner path so `H_P,H_S` lie in its maximal erosion;
2. move the two hosts to exterior positions while transporting the two
   outward traces; or
3. admit the nonflat stutter walk and give one simultaneous owner/lower/deck
   replacement plus common-cap Hall certificate.

For a strict upper-exact Catalan route, every option additionally needs an
upper rethread replacing at least `8d+7` folded incidences (`8d+8` on the
canonical aligned face).  This prerequisite is separate from owner planting,
residence, and the pointwise source-cap identities.

In every case the two hosts must be handled jointly: their distance `d` is
exactly what cancels rank in (4.1), while either host alone has the universal
rank-`r-1` split valley.

## 7. Replay

Run

```text
python3 scratch/audit_ad_c8_folded_two_ray_host_owner_gate_20260801.py --write
```

The independent replay checks `5<=d<=12`, all folded common-cut candidates,
the separated aligned counts and positions, unique mixed-owner incidence,
the distance-`d` equality bound, both host modes, exact ranks,
the forced stutter, residence, owner/lower/upper palette counters, common
pointwise source caps, lost old cells, and (5.4).  The primary upstream
`audit_depth` wrapper is independently passing; this replay tests the
additional enlarged aligned-and-upper-support-safe face as well as the
canonical aligned face.
