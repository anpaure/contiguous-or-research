# Twisted heptagons: the fixed-root load obstruction, mobile-root checksum thinning, and balanced backup load

**Date:** 2026-08-02  
**Lane:** A, bounded-load completed tickets for the protected Pascal/pull-ear recurrence  
**Status:** exact fixed-root no-go; exact central mobile-root subatlas; exact
equitable duplicate-backup extension under a demand-load hypothesis.  The
remaining history/two-state-exposure hypothesis is stated explicitly.  No
finite search is used.

## 0. Result and scope

Let `k` be odd, let `rho` be a cyclic coordinate action, and let `h` be
coprime to `k`.  A seven-run rank-`r` root `X` has

\[
 |X\setminus\rho^hX|=|\rho^hX\setminus X|=7.             \tag{0.1}
\]

The raw twisted count does not itself have the desired one-degree resource
load.  In fact, for a fixed root pair `(X,rho^hX)`, every seven-step
geodesic is contained in a set of only `3432` moving owners.  Thus a
rooted list of order `k^7` necessarily has a moving-owner token of load
order `k^7`, even before history or caps are attached.

There is, however, an exact one-degree repair at the *prospective central*
level.  Use a linear family of mutually separated seven-run roots, one
geodesic per root, and take one additive checksum slice of the seven
retained-label choices.  This gives

\[
 |\mathcal A|=\Omega(k^7),\qquad
 \Delta_{\rm moving}(\mathcal A)=O(k^6),\qquad
 \Delta_{\rm decorated}(\mathcal A)=O(k^5).             \tag{0.2}
\]

Every central cap depending on one retained label already has load
`O(k^5)`.  Duplicate-provider paths need not be installed in every atlas
alternative.  For a fixed number of finally selected tickets, the protected
provider theorem installs all named backups *after selection*.  Hence
provider-owner/facet loads are not part of the alternative-atlas conflict
degree.  This separation has a crucial physical qualification: the theorem
applies only when the actual protected incidence bank obeys
`L+2q<=m-2`.  A full coprime-voltage development has at least `14k`
packet-incidence edges and is not such a bank.  Applying the provider theorem
to a developed quotient packet requires a new equivariant extension theorem,
or a compound which returns its cap current before physical development.

What remains unproved is exactly the following correlation row:

> a fixed task/socket must admit `Omega(k)` genuinely different rooted
> old/new pull exposures, with compatible bi-history collars whose physical
> occurrence load is bounded independently of the root.

The theorem that an `O(d)` collar and `O(d)` named backups extend to a
terminal two-factor does not imply this row.  It is a one-state terminal
extension theorem, not a common-incumbent pull-ear exposure theorem.

## 1. The fixed-root moving-geodesic obstruction

Put

\[
 D=X\setminus\rho^hX,\qquad I=\rho^hX\setminus X.
\]

Then `|D|=|I|=7`.  Every rank-preserving shortest Johnson path from `X` to
`rho^hX` has an intermediate owner of the form

\[
                  X-D'+I',\qquad D'\subseteq D,
                  \ I'\subseteq I,\quad |D'|=|I'|.      \tag{1.1}
\]

### Theorem 1.1 (fixed-root one-degree load is impossible)

Let `mathcal T` be any multiset of `N` labelled seven-step geodesic tickets
with the same endpoint pair `(X,rho^hX)`.  Count the six strict internal
moving owners as resources.  Then some internal moving owner has load at
least

\[
                         {6N\over3430}.                  \tag{1.2}
\]

Consequently, if `N>=c k^7`, no bound `Ck^6` is possible for all moving
resources once `k>3430C/(6c)`.  This remains true after arbitrary thinning
of retained-label, cap-backup, or history decorations.

#### Proof

By Vandermonde,

\[
 \#\{X-D'+I':|D'|=|I'|\}
   =\sum_{j=0}^7{7\choose j}^2={14\choose7}=3432.        \tag{1.3}
\]

After deleting the two endpoints there are at most `3430` possible strict
internal owners.  Every seven-step path contributes six incidences to this
set.  Averaging gives (1.2).  Decorations do not change these owners.
\(\square\)

Thus calling only `X` and its first facet private is insufficient.  One
must either declare the entire `3432`-owner geodesic closure private, or
expose `Omega(k)` genuinely different endpoint pairs.  Quantitatively, any
atlas of size `ck^7` and moving load at most `Ck^6` needs at least

\[
                         {6c\over3430C}k                \tag{1.4}
\]

different fixed-root closure classes.

## 2. A linear separated family of seven-run roots

Read coordinates in `rho^h` order.  Assume

\[
             \min\{r,k-r\}\ge\epsilon k                \tag{2.1}
\]

for a fixed `epsilon>0`, and fix one legal deleted boundary coordinate
`a`.  For all sufficiently large `k`, there is a family

\[
                    X_1,\ldots,X_s,\qquad
                    s\ge {\epsilon k\over40},           \tag{2.2}
\]

such that:

1. every `X_t` has seven positive runs and `a in X_t-rho^hX_t`;
2. `d_J(X_t,X_u)>=18` for `t ne u`.

#### Construction and proof

Reserve a constant interval containing six isolated singleton one-runs,
one of them ending at `a`.  In the complementary linear corridor put one
one-run of length `r-6`.  The unused zero slack in that corridor is
`k-r-O(1)`.  Translate the long run in steps of `18`, retaining a zero at
both corridor ends.  This gives at least `(k-r-O(1))/18` words.  Two words
whose long intervals are displaced by `18j` have Johnson distance
`min(18j,r-6)>=18`.  The constant loss in (2.2) is valid for large `k`.
\(\square\)

Choose one deletion order and one insertion order for every `X_t`, and let
`G_t` be the resulting seven-step geodesic.  Every moving owner of `G_t` is
within Johnson distance seven of `X_t`.  Hence moving-owner sets belonging
to different `t` are disjoint.  More strongly, two such moving owners have
distance at least four.  Therefore no retained owner, common facet, or
immediate cap incident with one moving owner can coincide with the
corresponding central resource of another `G_u`: equality of those
resources would put the moving owners at distance at most two.

The same construction survives an `O(d)` collection of unary boundary
forbidden labels when `d=o(k)`: choose the six fixed singleton positions
outside the forbidden set, and discard translations for which either end
of the moving long run hits it.  Each forbidden coordinate removes at most
two translations.  This statement applies only to literal unary guard
constraints; it is not a replacement for a general bi-history relation.

## 3. Checksum thinning of the seven retained labels

Fix `t`.  At row `i`, let `A_(t,i)` be the legal set of retained extension
labels after simplicity, marker and declared unary history exclusions.  We
use the following exact hypothesis:

\[
                         |A_{t,i}|\ge {\epsilon k\over2}
                    \quad(0\le i<7).                    \tag{3.1}
\]

This follows from the raw `k-r-1` extension choices whenever at most
`O(d)=o(k)` values are forbidden per row.  It does not follow for an
arbitrary relation-labelled exterior.

Greedily choose pairwise-disjoint sets

\[
 B_{t,i}\subseteq A_{t,i},\qquad
 |B_{t,i}|=b:=\left\lfloor{\epsilon k\over28}\right\rfloor.
                                                               \tag{3.2}
\]

Indeed, before the last choice fewer than `6b` values have been used, and
`epsilon k/2-6b>b` for large `k`.

Partition `prod_i B_(t,i)` by the value of

\[
                         z_0+\cdots+z_6\pmod k.          \tag{3.3}
\]

Choose a largest fibre `mathcal Z_t`.  Then

\[
             |\mathcal Z_t|\ge {b^7\over k},qquad
             |\mathcal Z_t|\le b^6.                    \tag{3.4}
\]

For every fixed position `i` and fixed value `z`,

\[
       \#\{\boldsymbol z\in\mathcal Z_t:z_i=z\}\le b^5. \tag{3.5}
\]

The upper bounds follow because six coordinates determine the seventh in
(3.3), and after fixing one coordinate, five coordinates determine the
sixth remaining one.  Any unintended equality among a fixed finite list of
retained owners, caps, or row options fixes two displayed extension labels;
it therefore removes only `O(b^5)` tuples.  Deleting all such tuples leaves
at least `b^7/k-O(b^5)=Omega(k^6)` tickets per root.

### Theorem 3.1 (prospective mobile-root subatlas)

Under (2.1) and (3.1), the union over the roots in Section 2 contains a
simple prospective twisted-heptagon subatlas `mathcal A` such that

\[
 |\mathcal A|\ge c_\epsilon k^7,\qquad
 \max_q \deg_{\mathcal A}(q)\le C_\epsilon k^6          \tag{3.6}
\]

for every moving owner, moving facet, and fixed geodesic row resource, and

\[
 \max_q \deg_{\mathcal A}(q)\le C_\epsilon k^5          \tag{3.7}
\]

for every nonanchor central resource which fixes one retained label.

One may take, for all sufficiently large `k`,

\[
 c_\epsilon={\epsilon\over80}
              \left({\epsilon\over56}\right)^7,\qquad
 C_\epsilon=\left({\epsilon\over28}\right)^6+1.         \tag{3.8}
\]

#### Proof

Use at least `epsilon k/40-O(d)` legal roots and at least
`b^7/k-O(b^5)` decorations per root.  For large `k` the conservative
constant in (3.8) follows.  A fixed geodesic resource occurs in at most all
`b^6` decorations of its root and in no other root.  A resource revealing
one `z_i` has load at most `b^5` by (3.5).  Section 2 excludes cross-root
central collisions.  \(\square\)

This proves the desired one-degree load for the *central prospective*
projection.  It deliberately uses root mobility; it does not contradict
Theorem 1.1.

## 4. Exact postselection of duplicate-cap providers

Write `m=(k+1)/2`.  Suppose a *finally selected* fixed-size packet bank has
a compatible 2-bounded protected incidence graph `P`,

\[
 |E(P)|=L,
\]

and a list `Q` of `q` named cap requests, counted with multiplicity.  The
provider theorem gives the following exact conclusion.

### Theorem 4.1 (provider resources separate after ticket selection)

If

\[
 {m+1-v_O(P)-2q\choose2}>v_F(P)+q                     \tag{4.1}
\]

and

\[
                         L+2q\le m-2,                   \tag{4.2}
\]

then all `q` duplicate providers can be chosen mutually vertex-disjoint and
disjoint from `P`, and the enlarged bank extends to a spanning owner/facet
two-factor.  In particular, when `L,q=O(d)` and `d=o(m)`, both inequalities
hold for all sufficiently large `m`.

Consequently provider owners, provider facets, and provider incidences do
not have to be assigned to all `Omega(k^7)` alternatives.  First select a
bounded number of compatible central/history tickets using their named cap
request lists; then apply (4.1)--(4.2) once to their union.  This removes the
provider occurrences from the atlas load calculation.

#### Proof

This is the protected duplicate-cap theorem applied to the union of the
selected banks.  A cap has provider graph `K_(m+1)`.  Before the last greedy
choice, the forbidden owner and facet counts are bounded by the left and
right sides of (4.1); every provider contributes two incidence edges, giving
(4.2).  \(\square\)

The named cap **keys** remain part of the alternative ticket.  In the
checksum atlas, a central cap `x_i+z_i` has load `O(k^5)` by (3.5), while a
root-private collar cap has load at most `O(k^6)`.  If one nonprivate named
cap key is frozen across all `Omega(k^7)` alternatives, that key itself has
load `Omega(k^7)`; postselected provider multiplicity cannot repair it.

There is also a decisive development qualification.  The theorem above is
literal and physical.  A free coprime-voltage development of one quotient
heptagon contains at least `14k` protected packet-incidence edges before
collars or backups.  Since `14k>m-2`, (4.2) fails.  Thus Theorem 4.1 applies
to a literal `O(d)` terminal packet/collar bank, but not automatically to the
whole developed twisted packet.  A quotient-equivariant protected extension
or a cap-returning compound is still required.

## 5. What is and is not a completed regenerative atlas

Call a boundary family **mobile-history exposed** if the `Omega(k)` roots of
Section 2 can be supplied with literal old/new retained ears such that:

1. each resulting heptagon passes the exact forward/reverse history-ticket
   relation for the admitted socket;
2. every collar resource is used by only `O(1)` root classes, or otherwise
   fixes one checksum label;
3. every nonprivate named cap demand has base-atlas load `O(k^6)` and the
   finally selected literal physical bank satisfies (4.1)--(4.2); and
4. the old and new rows are exposed relative to one common regenerative
   state (or by an explicitly returned compound pull), rather than by two
   unrelated terminal completions.

### Corollary 5.1 (conditional postselectable-ticket theorem)

If a task/socket is mobile-history exposed, (2.1), (3.1), and the provider
hypotheses of Theorem 4.1 hold, then it has `Omega(k^7)` coprime-voltage
ticket candidates, each using `O(d)` central/history resources and carrying
a named cap-request list, and every nonprivate moving, history, and
cap-demand key has load `O(k^6)`.  After any fixed-size compatible
selection, Theorem 4.1 installs the literal backup-provider paths and
completes the selected terminal banks.

The constants are those of (3.8), multiplied only by the fixed overlap and
guard constants in the mobile-history exposure.

#### Proof

Theorem 3.1 handles the moving and decoration-dependent resources.
Mobile-history exposure handles the occurrence-labelled collar resources
and makes the tickets transitions from the same regenerative state.
Theorem 4.1 attaches backups after selection, so their provider resources
are not coordinates of the alternative-atlas load bound.
The fixed-depth completed-ticket composition theorem then supplies the exact
cap/history state update.  \(\square\)

The alternatives above are not individually literal provider-completed
tickets; they are the reduced postselectable interface justified by Theorem
4.1.  The new provider theorem proves the terminal-host and backup part of
this corollary.  It does **not** prove mobile-history exposure: its
completion is chosen separately for each terminal protected bank, it need
not contain the old packet rows, and it need not give the same retained ears
or exterior history relation.  Hence Corollary 5.1 is not presently
unconditional.

## 6. Sharp next actuator

Theorem 1.1 identifies the smallest missing degree.  A fixed-root primitive
has no one-degree-load subatlas of size `Omega(k^7)`.  Any replacement must
export at least one **mobile root parameter** taking `Omega(k)` values.  A
minimal prospective compound is therefore

\[
  \text{root-relocation ear}\ ;\
  \text{twisted }C_{14}\ ;\
  \text{return/root-state transport},                  \tag{6.1}
\]

where the relocation choices give pairwise separated root pairs and the
whole compound returns the same Pascal aperture, cap-surplus class, and
bi-history socket.  Sections 2--4 prove that, once such a physical
relocation/return family exists with `O(d)` support and bounded collar
overlap, no further central or duplicate-backup load obstruction remains.

Constructing (6.1), or proving a mobile old/new exposure theorem directly,
is the exact residual supply gate.  Raw seven-run abundance, marginal cap
providers, and independent terminal two-factor completions do not imply it.

## 7. Provenance

This note uses only the exact interfaces in:

- `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`;
- `MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md`;
- `MATH_THEOREM_HEPTAGON_PROTECTED_HOST_AND_DUPLICATE_CAP_BACKUPS_20260802.md`;
- `MATH_THEOREM_A_EQUIVARIANT_DIRECTED_HISTORY_EAR_SEMIGROUPOID_AND_PULL_TRANSPORT_20260802.md`; and
- `MATH_THEOREM_BALANCED_CAP_BACKUP_AND_BOUNDARY_HISTORY_REGENERATION_20260802.md`.

It makes no frozen-factor neighbourhood, old/new common-host, deeper-upper,
source, compiler, or universal-word claim.
