# Monotone pivot insertion gives one exact common-Q matching under an occurrence-labelled release state

Date: 2026-08-01  
Lane: R, pivot occurrence/common-cap audit  
Status: unconditional local transport and matching theorem; exact
common-`Q` criterion; explicit exported state and sharp omitted-field
counterexamples.  Physical rank-saturated host existence, owner/q1 topology,
residence and regeneration remain separate.

## 0. Verdict

Let the old source have a cut

\[
                 \cdots,Q_L\mid Q_R,\cdots
\]

and insert one nonempty letter `X`:

\[
                 \cdots,Q_L,X,Q_R,\cdots .             \tag{0.1}
\]

If

\[
                         X\subseteq Q_L\cup Q_R,        \tag{0.2}
\]

the monotone convex-hull map injects every old interval address and preserves
its literal OR.  In the width-`h` band its complement is exactly the
singleton pivot plus two rays, while exactly `h-1` old crossing cells of
width `h` map to width `h+1`.

For a fixed old matching the exact condition is therefore not a new Hall
theorem.  Release every logical target vertex reassigned to a ray cell,
require the retained old matching to avoid the `h-1` escaped cells, and
inject the released/fresh packet targets into the literal fan cells.  The
union is then one exact target-to-cell matching.  If all matching, owner and
guard rows are written in one fixed cap state and are realized by the
inserted source word, the maximal common-`Q` theorem makes them one exact
common-`Q` system.

Two qualifications are load-bearing.

1. Both rays are private for the **monotone convex-hull map**.  If one calls
   (0.1) a canonical full-block refinement of `Q_L` (or of `Q_R`), the ray
   on that grouped side lies in the full-block image.  It becomes usable
   only after its old target vertices are released.  No one grouping makes
   both rays private simultaneously.
2. “Occurrence-labelled multiset” and “one target per mask” are different
   matching models.  The release set must use the actual target-node
   identities.  Repeated equal-mask ray rows are either distinct occurrence
   nodes, each needing a cell, or redundant equality constraints on one
   ordinary target vertex; they cannot silently change interpretation.

Thus the pivot does give the claimed exact common-`Q` matching, but only in
the exported state specified in Section 5.

## 1. Literal monotone transport and exact fan complement

Index the old cut as

\[
 \ldots,A_{-2},A_{-1}\mid A_1,A_2,\ldots
\]

and the new pivot by position `0`.  For an old interval `I`, define
`Phi(I)` by shifting a right-only interval one position, leaving a left-only
interval fixed, and taking the new convex hull for a crossing interval.

### Theorem 1.1 (addressed monotone injection)

Condition (0.2) is necessary and sufficient for

\[
                      \operatorname{OR}(\Phi(I))
                      =\operatorname{OR}(I)            \tag{1.1}
\]

for every old interval `I`.  The map `Phi` is injective on literal interval
addresses.

#### Proof

Only a crossing interval acquires `X`, and it contains both `Q_L,Q_R`.
Thus (0.2) makes `X` redundant in every such OR.  Conversely the adjacent
two-letter interval forces (0.2).  Deleting the new pivot from a crossing
image, and undoing the right shift on a right-only image, recovers the old
address uniquely.  \(\square\)

Let `C_h^-` and `C_h^+` be the old and new cells of width at most `h`.
Assume that the cut has at least `h` old source positions on each side, as
it does in the displayed sharp block.  At a clipped endpoint the same
statement holds with the escaped-cell and ray lists truncated.
There are exactly `h-1` old width-`h` cells which cross the cut; call this
set `E_h`.  Let `F_X` consist of the singleton pivot, the `h-1` cells ending
at the pivot from the left, and the `h-1` cells starting at the pivot to the
right.

### Theorem 1.2 (band decomposition)

\[
 \Phi:\ C_h^-\setminus E_h\hookrightarrow C_h^+,
 \qquad
 C_h^+\setminus\Phi(C_h^-\setminus E_h)=F_X,          \tag{1.2}
\]

and `|F_X|=2h-1`.  Every cell in `E_h` maps to width `h+1`; no other old
band cell leaves the band.

The ray values are the literal cumulative unions

\[
 X,\qquad X\cup A_{-1}\cup\cdots\cup A_{-t},\qquad
 X\cup A_1\cup\cdots\cup A_t\quad(1\le t<h).         \tag{1.3}
\]

#### Proof

An old crossing cell gains exactly one position.  It leaves the band iff its
old width was `h`, giving `E_h`.  A new band cell outside the image must
contain the pivot and have no old positions on one of its two sides; these
are precisely the singleton and two rays.  \(\square\)

## 2. Exact target-release matching theorem

Target vertices below are occurrence-labelled.  In the ordinary compiler,
where one vertex represents each mask, take the occurrence ID to be the mask
itself.

Let

\[
             M_0=\{(s,c_s):s\in L\}                  \tag{2.1}
\]

be an old matching into `C_h^-`.  Let `U` be a subset of `L` consisting of old target
vertices deliberately released for packet use, let `D` be genuinely fresh
packet target vertices, and let

\[
               \psi:U\mathbin{\dot\cup}D\hookrightarrow F_X 
                                                               \tag{2.2}
\]

be an injection satisfying

\[
                   \operatorname{OR}(\psi(s))=\operatorname{value}(s).
                                                               \tag{2.3}
\]

Assume

\[
                         c_s\notin E_h\qquad(s\in L\setminus U).
                                                               \tag{2.4}
\]

### Theorem 2.1 (exact combined matching)

Then

\[
 M^+=\{(s,\Phi(c_s)):s\in L\setminus U\}
      \mathbin{\dot\cup}
      \{(s,\psi(s)):s\in U\mathbin{\dot\cup}D\}      \tag{2.5}
\]

is an injective literal matching saturating `L union D`.

Conversely, for the prescribed maps `Phi,psi`, conditions (2.2)--(2.4) and
target-ID consistency are necessary.

#### Proof

The first bank is injective by Theorem 1.1 and lies in the band by (2.4).
The second is injective by (2.2).  The two cell banks are disjoint by
(1.2).  Their target shores are disjoint after the logical release `U`.
Equation (1.1) proves every transported equality and (2.3) proves every
packet equality.  Necessity is immediate for these fixed maps. \(\square\)

For a fixed `M_0`, condition (2.4) is the exact escaped-cell test.  The
rank-saturated hypothesis from the pivot theorem is a useful uniform
sufficient condition: if every cell in `E_h` has middle rank `m`, a matching
of strict-lower targets cannot use it.  Rank saturation is not necessary
when the actual matching simply avoids `E_h`.

### Equal-mask multiplicities

If `U` and `D` together have several occurrence IDs with one mask `S`, (2.2)--(2.3)
require at least that many distinct fan cells of value `S`.  In the ordinary
distinct-mask compiler there is one target vertex `S`; further ray cells of
value `S` are redundant protected rows, not additional matching edges.
This is the exact interpretation of the fan multiplicity inequalities.

### Corollary 2.2 (prepared common-core pivot)

Suppose the two adjacent host letters both contain one fixed core `Q`, and
\(X\subseteq Q\).  Every non-singleton fan interval contains its adjacent
host, so `X` is redundant there.  Each left/right ray target is exactly the
value of its old one-sided interval before insertion.  In the ordinary
compiler these are old logical target vertices, not fresh targets.  This
includes the sharp word: its outer `lambda` and `rho` letters are
singletons and need not contain `Q`.

Therefore take `U` to be the union of the two ray target sets, and also put
the singleton target `X` in `U` when `X` was already a target vertex of
`M_0`.  If `X` was absent, it is the only genuinely new target.  Assign all
released vertices to their natural fan cells.  If both chains are strict
and are also cross-bank distinct, the `2(h-1)` non-singleton masks are
pairwise distinct, so (2.2) is automatic.  The disjoint `lambda` and `rho`
banks of the sharp word give this stronger property.  Otherwise the
equal-mask multiplicity rule above is the exact test.  Formula (2.5) then
gives the desired complete matching.

The old matching equalities for released targets may remain in the common-Q
row family as redundant protected witnesses.  They are not second matching
edges incident with the same target vertex.

## 3. Full-block language versus monotone language

Suppose more strongly that \(X\subseteq Q_L\cap Q_R\), as in the prepared
`Q/L | Q/R` pivot.

* Grouping `(Q_L,X)` as a replacement block for `Q_L` is a valid full-block
  refinement.  The left pivot ray is then in the transported full-block
  image; the singleton and right ray are private.
* Grouping `(X,Q_R)` is symmetric.
* The monotone map `Phi` of Theorem 1.1 leaves one-sided old cells one-sided.
  Under `Phi`, both rays and the singleton form the private complement
  `F_X`.

Hence “full-block transport makes both rays private” is false literally.
There are two correct implementations:

1. use `Phi`, in which case Theorem 2.1 applies directly; or
2. use a one-sided full-block map, require every chosen packet cell to be
   disjoint from the retained full-block image, and release every old
   matching edge whose full-block image is one of those chosen cells.

In the ordinary one-vertex-per-mask sharp packet, releasing the ray target
vertices supplies exactly that disjointness.  With occurrence-labelled
equal-mask copies one must inspect the selected preimage edges explicitly.
Set-value identities alone do not choose between the two address maps.

## 4. One exact common-Q system

Fix one physical pivot state.  Let `C_p` be its source cap and `L_p` its
pointwise lower bound at every new position.  Let \(\mathcal R\) contain all
required rows:

* the matching equalities in `M^+`;
* every new fixed-width owner row;
* every retained protected row with its transported address;
* every redundant packet equality one elects to preserve; and
* all lower/upper cut and boundary rows required by the physical packet.

For \(R\in\mathcal R\), write `S_R` for its target, `J_R` for its live source
interval and `B_R` for its fixed exterior contribution.  Define

\[
 K_p=C_p\cap\bigcap_{R:p\in J_R}S_R.                 \tag{4.1}
\]

### Theorem 4.1 (common-Q criterion and pivot witness)

The row family has one exact common-`Q` realization iff

\[
 L_p\subseteq K_p\ne\varnothing
                 \quad\hbox{for every live }p,        \tag{4.2}
\]

and

\[
 S_R=B_R\cup\bigcup_{p\in J_R}K_p
                  \qquad(R\in\mathcal R).            \tag{4.3}
\]

In particular, if the literal inserted word in (0.1) lies between `L` and
`C` and literally realizes every declared row in \(\mathcal R\), then
(4.2)--(4.3)
hold.  Therefore Theorem 2.1 and one complete literal row replay really do
give **one simultaneous common-Q matching**, not merely separately feasible
matching and cap statements.

#### Proof

Equations (4.2)--(4.3) are the maximal-word common-`Q` criterion.  For the
last assertion, every actual source letter contains its lower bound and is
contained in its cap and in every incident target, hence in `K_p`; so
(4.2) holds.  Enlarging from
the actual word to `K` remains inside every incident `S_R`.  Its union on a
row contains the actual reconstruction `S_R` and is contained in `S_R`,
giving equality. \(\square\)

This proof is one-word and one-state.  Two phase words sharing only marginal
signatures do not thereby share one common cap.  If every live address must
carry the same letter in both phases, put both phase row families into the
single definitions (4.1)--(4.3).  If some addresses are phase-private,
export the common/private partition and use the mixed maximal-word
criterion: one `K_p^C` intersecting both phase row families at common
addresses and separate `K_p^epsilon` at private addresses, all below one
declared cap vector.  A common target allocation additionally needs paired
target and paired physical-address shores; two marginal phase matchings are
not enough.

## 5. Minimal exported pivot state

The following tuple is sufficient and, field by field, necessary for the
claimed interface:

\[
 \Theta_{\rm pivot}=
 (A^-,A^+,h,p,Q_L,Q_R,X;\ \Phi,E_h,F_X;\ M_0,U,D,\psi;\
   \mathcal J,L,C,\mathcal R;\ \Gamma).               \tag{5.1}
\]

Here:

1. `A^-,A^+` are the complete addressed old word and its literal inserted
   word.  The fields `h,p,Q_L,Q_R,X` fix the cut, orientation, old adjacent
   letters and inserted nonempty letter, including (0.2).
2. `Phi,E_h,F_X` fix the literal old-address transport, escaped cells and
   private fan addresses.  A one-sided full-block implementation must be
   named instead of `Phi` when used.
3. `M_0,U,D,psi` fix target-node identities, logical releases and the
   packet-cell injection.  Equal masks do not identify occurrence IDs.
4. \(\mathcal J\) lists every pivot owner window, including both endpoints,
   with its exact owner value, rank, occurrence identity and any required
   simplicity/Johnson-adjacency data.  Rank saturation of only the interior
   escaped cells does not certify these endpoint/adjacency rows.
5. \(L,C,\mathcal R\) are the complete lower-bound/cap vectors and
   row-incidence ledger used in (4.1)--(4.3), including owner, matching, cut
   and redundant protection rows and every fixed exterior contribution
   `B_R`.
6. `Gamma` maps every protected old occurrence guard to its new guard.  It
   must record at least address, width/type and any chronology/trace label.
   Crossing intervals gain one position under `Phi`; an exact-width guard
   therefore needs explicit permission or rehosting even though its OR is
   unchanged.

Owner simplicity, q1 palettes, topology, residence and regenerative charge
may be stored in \(\mathcal R\) only when they are literal OR rows.  Their
graph/run aspects remain separate fields of the outer physical state.

## 6. Sharp omitted-field failures

Each field in (5.1) has a two-line obstruction.

* Without (0.2), the adjacent crossing interval gains a new coordinate.
* Without (2.4), a retained matched width-`h` crossing cell moves outside
  the permitted band.
* Without release `U`, an old target vertex and its packet edge both occur
  in (2.5), so the union is not a matching on the target shore.
* Without occurrence IDs, two equal-mask obligations can be mistaken for
  one target or one target can be counted twice.
* Without cap/row state, take a pivot cap omitting one element of `X`; all
  interval OR identities remain true, but no legal source letter exists at
  the pivot.
* Without guard transport, a retained crossing occurrence of width `w<h`
  becomes width `w+1`; it remains in the band but an exact-width or
  exact-address guard can fail while the target value survives.
* Without rank/owner legality, a new `(h+1)`-window may have rank below the
  middle layer.  This is the rank-saturated-cut obstruction, independent of
  matching transport.

The rank obstruction already respects the prepared common-core form.  Take
`h=2`, middle rank four, `Q={q}`, `X={q}`, and the old local word

\[
             \{c\},\ Q\cup\{a\}\mid Q\cup\{b\},\ \{c\}.
\]

Its two old length-three windows have rank four, but the new central window
has value `{q,a,b}` of rank three.  The old crossing width-two cell has that
strict-lower value and escapes the band, so a matching using it fails.  By
contrast, a named matching supported on a one-sided cell still transports;
this is the sharp reason rank saturation is sufficient uniformly but not
necessary for fixed `M_0`.

The full-block wording fails at the smallest depth too.  For `h=2`, group
the insertion with the left host.  The old singleton address at that host
has full-block lift equal to the unique left-ray address.  Retaining that
old edge and simultaneously calling the left ray private creates a literal
cell collision.  The monotone map avoids it, while the full-block map needs
the corresponding edge release.

## 7. Independent replay

The dependency-free replay

```text
scratch/audit_r_monotone_pivot_occurrence_commonq_20260801.py
scratch/r_monotone_pivot_occurrence_commonq_20260801.audit.json
```

checks `2<=h<=64`.  It enumerates every old/new interval address, proves
literal injectivity and OR preservation, reconstructs the exact band
complement and `h-1` escaped cells, performs a target-release matching union,
and builds the componentwise maximal word for the simultaneous family of all
transported old rows, all fan rows and every new owner window.  It is a
formula audit on generic tagged letters, not a proof that a Pascal/PBBS
carrier supplies the required rank-saturated physical cut.
