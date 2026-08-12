# Source-opening penetration, truncated cut cores, and the PBBS height staircase

**Date:** 2026-08-05  
**Method:** pure cyclic interval mathematics; no computation or search  
**Status:** unconditional exact opening calculus.  It reduces the final
all-width upper opening to one truncated-core/height-staircase condition.
It does not prove that the canonical PBBS cycle, or a cycle obtained from
the present hybrid clean-C6 moves, satisfies a bounded staircase defect.

## 0. Outcome

Let

\[
 A=(A_i)_{i\in\mathbb Z_W}
\]

be a cyclic nonempty source word and let its depth-`d` owner cycle be

\[
 T_i=\bigcup_{j=0}^{d}A_{i+j}.
\tag{0.1}
\]

Opening before `A_0` and appending the first `d` source letters gives the
standard word of length `W+d`.  It retains every owner and every cyclic
source cell of width at most `d+1`.  It need not retain an arbitrary-width
upper owner interval.

For `C>=0`, append instead the first `d+C` source letters.  For a cyclic
owner witness of `q+1` owners, the extra `C` letters erase exactly the last
`C` edges of its ordinary cut obstruction.  This gives an exact targetwise
truncated core `K_C(Y)`.  The length-`W+d+C` prefix-copy opening is
upper-complete if and only if some cut lies outside every `K_C(Y)`.

After choosing one witness per target, the exponentially large condition
collapses to a height word `h` on the owner starts.  A cut before owner `c`
works with `C` extra letters exactly when

\[
 \boxed{h_{c-1-t}\le C+t\qquad(0\le t<u),}
\tag{0.2}
\]

where `u` is the largest selected owner depth.  Thus:

* `C=0` asks for the exact triangular safe-opening staircase;
* `C=1` asks for the staircase `1,2,3,...` immediately before the cut;
* `B(k)+O(1)` on this route is equivalent to a uniformly bounded
  staircase defect; and
* on the lower-middle PBBS orientation the fixed section has abstract scalar
  defect exactly one, while on the **upper-middle complement orientation
  used by the odd-word carrier** it has abstract scalar defect zero; without
  a new occurrence-preserving PBBS ordering theorem neither scalar ordering
  is yet a physical opening theorem.

The fixed PBBS gap-potential section supplies an explicit all-depth upper
witness bank inside the uncut canonical factor.  Formula (0.2) applies if
those occurrences remain consecutive in the terminal cycle.  The
resident/common-history hybrid preserves the lower compiler and complete
**internal cyclic** packet decks, but it does not transport that exterior
upper bank occurrence by occurrence and does not control the exterior
opening height word.  This is the precise remaining quantifier.

## 1. Source intervals and owner intervals

All indices in this section are cyclic modulo `W`.  An occurrence-labelled
owner witness is a pair `(i,q)`, `q>=0`, with value

\[
 U(i,q)=\bigcup_{s=0}^{q}T_{i+s}.
\tag{1.1}
\]

It uses `q+1` owners and has `q` internal owner edges.  Associativity and
(0.1) give the exact source identity

\[
 \boxed{
 U(i,q)=\bigcup_{p=0}^{d+q}A_{i+p}.}
\tag{1.2}
\]

Thus an owner interval of depth `q` is a source interval of width
`d+q+1`.  This distinction is essential: the first `d` appended source
letters retain each individual owner (`q=0`), but no crossing owner edge
(`q=1`) is retained merely for that reason.

Rotate the opening so that the cut is between indices `-1` and `0`, and
form

\[
 A^{[C]}=
 (A_0,A_1,\ldots,A_{W-1},A_0,A_1,\ldots,A_{d+C-1}).
\tag{1.3}
\]

The word has length `W+d+C`.  Its consecutive depth-`d` owner windows are

\[
 T_0,T_1,\ldots,T_{W-1},T_0,T_1,\ldots,T_{C-1}.
\tag{1.4}
\]

The repeated owners in (1.4) are occurrences, not new owner labels.

### Lemma 1.1 (exact overhang)

Let `(i,q)` cross the opening cut.  Write

\[
 i=-1-t,
 \qquad 0\le t<q.
\tag{1.5}
\]

Then its source interval (1.2) occurs nonwrapping in `A^[C]` if and only if

\[
 \boxed{C\ge q-t.}
\tag{1.6}
\]

If `(i,q)` does not cross the cut, it occurs already in the first source
copy and needs no extra letter.

#### Proof

The owner interval starts `t+1` owners before the cut and ends
`q-t-1` owner steps after owner `0`.  Hence its repeated post-cut owner
starts are

\[
 0,1,\ldots,q-t-1,
\]

exactly `q-t` starts.  Equation (1.4) contains these precisely when
`C>=q-t`.

Equivalently, the last source letter required by (1.2) is
`A_(d+q-t-1)`, while (1.3) ends its repeated prefix at
`A_(d+C-1)`.  The same inequality follows. `square`

The quantity

\[
 \omega_c(i,q)=
 \begin{cases}
 0,&(i,q)\text{ does not cross cut }c,\\
 q-t,&i=c-1-t,\ 0\le t<q,
 \end{cases}
\tag{1.7}
\]

is the **right overhang** of this witness at cut `c`.

## 2. Truncated cut cores

Let `e_j` denote the cyclic owner edge from `T_(j-1)` to `T_j`.  For a
witness `(i,q)` and integer `C>=0`, define its `C`-fatal prefix by

\[
 F_C(i,q)=
 \begin{cases}
 \{e_{i+1},e_{i+2},\ldots,e_{i+q-C}\},&q>C,\\
 \varnothing,&q\le C.
 \end{cases}
\tag{2.1}
\]

The word "prefix" refers to the direction of the owner witness.  These
are exactly its first `(q-C)_+` internal edges, not all its internal edges.

Let `W(Y)` be the complete occurrence family of cyclic owner intervals
whose union is an upper target `Y`.  Put

\[
 \boxed{K_C(Y)=\bigcap_{(i,q)\in\mathcal W(Y)}F_C(i,q).}
\tag{2.2}
\]

The empty occurrence family gives `K_C(Y)=E(T)`; in the applications below
cyclic upper support makes every family nonempty.

### Theorem 2.1 (exact prefix-copy opening theorem)

For a cut `e_c`, the target `Y` has a nonwrapping occurrence in `A^[C]`
if and only if

\[
 e_c\notin K_C(Y).
\tag{2.3}
\]

Consequently all cyclically supported upper targets survive the same
length-`W+d+C` prefix-copy opening if and only if

\[
 \boxed{
 e_c\notin\bigcup_YK_C(Y).}
\tag{2.4}
\]

#### Proof

By Lemma 1.1, a witness `(i,q)` fails at `e_c` with `C` extra prefix
letters exactly when the cut is one of the first `q-C` internal edges of
that witness, namely when `e_c in F_C(i,q)`.  Every witness of `Y` fails
exactly when `e_c` lies in their intersection (2.2).  Negating gives
(2.3), and intersecting the survival conditions over all targets gives
(2.4). `square`

For `C=0`, (2.2) is the ordinary forced-cut core.  The new point is that
extra cyclic source letters do not remove an arbitrary subset of this
core: they truncate every directed witness from its **terminal** end.

### Definition 2.2 (upper opening penetration)

Define

\[
 \boxed{
 \chi(A,T)=
 \min_{c}\ \max_Y\ \min_{I\in\mathcal W(Y)}\omega_c(I).}
\tag{2.5}
\]

Equivalently, `chi(A,T)` is the least `C` for which the complement in
(2.4) is nonempty.  If the length-`W+d` prefix-copy word already contains
the complete lower compiler and all middle owners, then

\[
 \boxed{\nu(k)\le W+d+\chi(A,T).}
\tag{2.6}
\]

within this fixed source/owner construction.

This is an exact equality for the minimum extra length among **cyclic
prefix-copy openings** of this source.  A different terminal collar or a
new seam can create witnesses not represented in (2.5), so `chi` is not
claimed to be a lower bound for arbitrary words.

## 3. One selected bank collapses to a height staircase

Choose one rank-correct witness

\[
 \sigma(Y)=(i_Y,q_Y)
\tag{3.1}
\]

for every required upper target.  Put

\[
 h_i=\max\bigl(\{q_Y:i_Y=i\}\cup\{0\}\bigr),
 \qquad
 u=\max_i h_i.
\tag{3.2}
\]

For one start `i`, the fatal prefixes (2.1) are nested as `q` increases.
Therefore only `h_i` matters.

### Theorem 3.1 (height-staircase equivalence)

For the selected bank `sigma`, the least number of extra cyclic prefix
letters required at cut `e_c` is

\[
 \boxed{
 \delta_h(c)=
 \max_{0\le t<u}\bigl(h_{c-1-t}-t\bigr)_+.}
\tag{3.3}
\]

Equivalently, `C` extra letters retain every selected witness if and only
if

\[
 \boxed{
 h_{c-1-t}\le C+t
 \qquad(0\le t<u).}
\tag{3.4}
\]

In particular,

\[
 \chi(A,T)\le\min_c\delta_h(c).
\tag{3.5}
\]

#### Proof

A selected witness based `t+1` starts before the cut has overhang
`q_Y-t` by (1.7).  Among all selected witnesses at that start, the maximum
is `h_(c-1-t)-t`, with negative values irrelevant.  Starts at distance
greater than `u` cannot cross a selected witness.  Taking the maximum gives
(3.3), and comparison with `C` gives (3.4).  Retaining the selected bank
retains every target, which gives (3.5). `square`

The exact `C=0` condition is

\[
 h_{c-1}\le0,
 \quad h_{c-2}\le1,
 \quad\ldots\quad,
 h_{c-u}\le u-1.
\tag{3.6}
\]

This is the triangular safe-opening condition.  With one extra letter it
becomes

\[
 h_{c-1}\le1,
 \quad h_{c-2}\le2,
 \quad\ldots\quad,
 h_{c-u}\le u.
\tag{3.7}
\]

Thus a `B+1` proof on this route needs a physical `1,2,...` terminal
staircase, not merely all-depth cyclic support.

### Corollary 3.2 (quiet terminal block)

If the `L` starts immediately before cut `c` have height zero, then

\[
 \delta_h(c)\le(u-L)_+.
\tag{3.8}
\]

More generally, any terminal block satisfying

\[
 h_{c-1-t}\le C+t
 \qquad(0\le t<L)
\]

reduces the remaining black-box bound to `(u-L)_+`.

#### Proof

For `t<L`, the displayed hypotheses control (3.3).  For `t>=L`, use
`h<=u`, so `h-t<=u-L`. `square`

### Corollary 3.3 (exact scalar condition under arbitrary reordering)

Suppose only the cyclic order of the starts is left free, while their height
multiset is fixed.  Let

\[
 a_1\le a_2\le\cdots\le a_W
\tag{3.9}
\]

be the sorted heights.  The least possible staircase defect over all cyclic
orders is

\[
 \boxed{
 C_{perm}=\max_{1\le j\le u}
            (a_j-(j-1))_+.}
\tag{3.10}
\]

In particular a permutation with defect at most `C` exists if and only if

\[
                         a_j\le C+j-1
                         \qquad(1\le j\le u).
\tag{3.11}
\]

#### Proof

The `u` starts immediately before the cut must be matched to thresholds

\[
 C,C+1,\ldots,C+u-1.
\]

Among all choices of `u` starts, the coordinatewise smallest sorted list is
`a_1,...,a_u`.  A matching to increasing thresholds exists exactly when
the sorted inequalities (3.11) hold.  Placing `a_j` at distance `j-1`
before the cut realizes them.  The least `C` satisfying all inequalities is
(3.10). `square`

This separates two gates sharply.  Formula (3.10) is the complete scalar
height-inventory test.  A PBBS proof must additionally realize the required
terminal order by owner-legal rethreading while retaining the witness
occurrences.  The resident hybrid currently proves neither arbitrary height
permutation nor that retained internal witnesses keep their old heights.

## 4. PBBS fixed-section application and its transport qualification

Put `n=2m+1` and let `g=f^2` be the canonical centered PBBS chronology on
rank-`m` states.  Its exact phase-complement identity is

\[
 U_q(X)=[n]\setminus L_{q-1}(fX).
\tag{4.1}
\]

The new gap-potential theorem supplies, inside this one fixed factor, a
corrected occurrence for every lower target at every depth.  Therefore it
also gives one explicit rank-correct upper witness for every proper upper
target:

* for `q=1` and `Y` of rank `m+1`, put `S=[n]\setminus Y`, take `Z=S`,
  and start the upper witness at `X=f^(-1)Z`;
* for `2<=q<=m` and `Y` of rank `m+q`, put
  `S=[n]\setminus Y`, of rank `m-(q-1)`, choose the fixed-section root
  `Z` with `L_(q-1)(Z)=S`, and again put `X=f^(-1)Z`.

Equation (4.1) proves that the `q+1` owner interval based at `X` has union
`Y`.  The full-ground target is witnessed by the whole opened owner path
and needs no cyclic cut protection.

There is a strong scalar consequence.  Let

\[
 \mathcal R=f^{-1}(\mathcal X_1),
 \qquad
 \mathcal X_1=\{\sigma_1(K):K\in{[n]\choose m-1}\}.
\tag{4.2}
\]

Every chosen witness of depth `q>=2` above starts in `mathcal R`, because
the same entrance-depth-one section is complete at every later depth.  The
depth-one upper row, on the other hand, uses every start exactly once: the
map sending `Y` to `f^(-1)` of its complement is a bijection on the `W`
middle starts.
Therefore the resulting height word satisfies

\[
 h_i=1\quad(i\notin\mathcal R),
 \qquad
 |\mathcal R|=N_1={2m+1\choose m-1},
\tag{4.3}
\]

and hence

\[
 \#\{i:h_i=1\}
 \ge W-N_1
 =\frac{2W}{m+2}
 \ge m.
\tag{4.4}
\]

For the final inequality, when `m>=2` use

\[
 W={2m+1\choose m}
   =\prod_{j=1}^{m}\frac{m+1+j}{j}
   \ge\frac{(m+2)(m+3)}2
   \ge\frac{m(m+2)}2;
\]

the case `m=1` is immediate.

### Theorem 4.1 (lower-middle orientation: abstract defect one)

For the fixed-section upper bank just constructed, the minimum staircase
defect after an arbitrary permutation of its occurrence-height tokens is
exactly one:

\[
                         \boxed{C_{perm}=1.}
\tag{4.5}
\]

#### Proof

Every start carries its depth-one upper target, so every height is at least
one.  Thus (3.10) gives `C_perm>=1`.  By (4.4), the `m=u` smallest
heights may all be chosen equal to one.  Hence

\[
 a_j=1\le j\qquad(1\le j\le m),
\]

and (3.11) gives `C_perm<=1`. `square`

Equivalently, if an owner-legal rethread can place `m` transported
height-one starts consecutively immediately before the final cut while
retaining every selected occurrence, then one additional cyclic source
letter preserves the whole upper bank.  No sorting of the higher heights
is required.

The upper-middle odd-word carrier face uses the complementary,
rank-`(m+1)` owner row.  On that row the scalar conclusion improves from
one to zero.

Put

\[
                         \overline X=[n]\setminus X.
\]

For every PBBS lower intersection,

\[
 \boxed{
 \bigcup_{t=0}^{q}\overline{g^tX}
   =[n]\setminus\bigcap_{t=0}^{q}g^tX
   =[n]\setminus L_q(X).}
\tag{4.6}
\]

Let `Y` be a proper upper target for the rank-`(m+1)` complement row, of
rank `m+1+q`, where `1<=q<=m-1`.  Its complement `S` has rank `m-q`.
The entrance-one common-section theorem gives
`X` in the start set defined in (4.2), with `L_q(X)=S`; hence (4.6) gives a
`q+1`-owner witness for `Y` based at the same position `X` in the
complement chronology.

Thus **every** proper upper target of the upper-middle complement owner row
may be assigned a witness whose start lies in the one entrance-one start
set.
Every start outside that set has height zero.  As before,

\[
 W-|\mathcal X_1|=\frac{2W}{m+2}\ge m>m-1.
\tag{4.7}
\]

### Theorem 4.2 (upper-middle complement: abstract defect zero)

For the fixed-section upper bank on the rank-`(m+1)` complement owner row,
the minimum staircase defect after arbitrary permutation of the
occurrence-height tokens is

\[
                         \boxed{C_{perm}=0.}
\tag{4.8}
\]

#### Proof

The maximum proper upper depth is `u=m-1`; the full-ground target survives
as the union of the complete opened owner path.  Equation (4.7) supplies at
least `u` height-zero starts.  Hence the `u` smallest heights in (3.10) are
all zero, and `C_perm=0`. `square`

Equivalently, an occurrence-preserving owner-legal rethread which puts
`m-1` of these height-zero starts consecutively immediately before the cut
would preserve every selected proper upper witness with the standard
`d`-letter deadline collar and **no** additive opening charge.

In fact the canonical PBBS factor already contains one whole component of
height-zero starts for this gap-potential section.

### Theorem 4.3 (the all-unit soliton is a literal quiet opening cycle)

Assume `m>=2`.  Consider the rectangular all-unit PBBS component with rooted
Dyck shape

\[
                         D=(10)^m.
\tag{4.9}
\]

It has length `n=2m+1`.  Every one of its outgoing starts lies outside the
entrance-one gap-section set `mathcal X_1`.  Consequently every start on
this component has upper-middle height zero.

#### Proof

Write a rooted middle state as

\[
                         A=0_r(10)^m.
\]

The distinguished deletion in the PBBS successor removes the first up-step
`p`; let `z` be the zero immediately after it.  The outgoing q1 core is

\[
                         K=0_r0_p0_z(10)^{m-1}.
\tag{4.10}
\]

Forward cyclic cancellation pairs every displayed `10` and leaves exactly

\[
                         U_+(K)=\{r,p,z\}.
\tag{4.11}
\]

For reverse cancellation, pair `z` with the first later one, then each
intervening tail zero with the next one.  If `w` is the final zero, the
three reverse-unmatched zeros are

\[
                         U_-(K)=\{r,p,w\}.
\tag{4.12}
\]

Use the gap-section convention `C,A` at a shared coordinate, with `A`
forward-unmatched and `C` reverse-unmatched.  Starting at `r`, the expanded
mark order is

\[
 C_r,A_r,C_p,A_p,A_z,C_w.
\tag{4.13}
\]

Therefore the three numbers of `A` marks in successive open `C` gaps are

\[
                         (1,2,0).
\tag{4.14}
\]

The potential increments `z_i-1` are `(0,1,-1)`.  Hence its unique maximum
is at `C_w`, and the last `A` before it is `A_z`.  The fixed gap section
selects the remote occurrence

\[
                         K+w\longrightarrow K+z.
\tag{4.15}
\]

The outgoing component edge is instead

\[
                         A=K+p\longrightarrow gA=K+r.
\tag{4.16}
\]

Indeed the gap immediately preceding `C_p` ends in `A_r`; (4.16) is the
corresponding nonmaximal boundary.  Thus the outgoing start `A` is not in
`mathcal X_1`.

The rooted `f` update fixes the shape `(10)^m` and advances its physical
root by one unit (equivalently, use the standard rectangular-soliton formula
with `u=1,b=m`).  The centered successor is `g=f^2`; since `2m+1` is odd,
its two-unit root advance still visits every rotation.  Thus the component
consists of all rotations of (4.10).  The maximum in (4.14) is unique, so
the same rejection holds at every rotation independently of the global tie
rule.  Every component start is therefore outside `mathcal X_1`. `square`

### Corollary 4.4 (protected quiet-root opening)

Protect any directed path of `m-1` consecutive starts on the all-unit
component.  Suppose a subsequent owner/source construction:

1. joins the complete factor into one terminal source cycle while retaining
   this path consecutively;
2. transports or recreates the selected upper witness bank without using a
   start in the protected path; and
3. retains the proved lower compiler and depth-`d` source relation.

Cut immediately after the protected path.  Then the standard `d`-letter
unroll, of length `W+d`, preserves every proper upper target, every owner,
and every lower compiler cell.

#### Proof

Theorem 4.3 makes all `m-1` preceding heights zero.  The maximum proper
upper depth is `u=m-1`, so (3.4) holds with `C=0`.  Theorem 2.1 preserves
the upper bank; the standard source collar preserves owners and lower cells.
`square`

The component has `2m+1` starts, so after protecting `m-1` of them there
remain `m+2` positions on which to place a root cut or bounded owner-level
port.  This is ample scalar room, but the current prospective resident
source packet has an additional halo and no theorem yet plants a global
fusion forest while avoiding the protected path.

On every unmodified canonical PBBS component this defines a concrete
occurrence-labelled witness bank.  If the canonical factor has already
been made into one source cycle without changing these consecutive
occurrences, or if a later rethread supplies an occurrence map carrying
them to consecutive terminal intervals, it defines a terminal height word
by (3.2), with `u<=m`.  The present fixed-section theorem alone supplies
neither of those topology/transport assertions.  Under that explicit
qualification we have:

### Corollary 4.5 (exact physical PBBS opening gate)

For a terminally consecutive image of the phase-shifted fixed-section upper
bank, a length-`W+d+C` prefix-copy opening exists whenever its height word
has a cut satisfying

\[
 h_{c-1-t}\le C+t
 \qquad(0\le t<m).
\tag{4.17}
\]

In particular, a uniformly bounded staircase defect proves

\[
 \nu(k)\le B(k)+O(1)
\tag{4.18}
\]

once the same cyclic source already carries the proved lower compiler and
owner row.  Zero defect gives the exact `B(k)` opening; defect one gives
`B(k)+1`.

The fixed-section theorem proves existence of the witness bank inside the
uncut canonical factor, but it does not prove terminal consecutiveness or
(4.9) for bounded `C`.  Its mortality and repeat ledgers count correct
occurrences; they do not transport them through an arbitrary rethread or
order the maximum selected depths around the final owner cycle.

### Corollary 4.6 (black-box bound from the stated inputs)

Because every selected proper PBBS upper witness has `q<=m`, appending the
first `d+m` source letters retains every selected witness at every cut.
Thus, once the qualified one-cycle occurrence bank above exists, its cyclic
source gives the prefix-copy estimate

\[
 \boxed{\nu(k)\le W+d+m}
\tag{4.19}
\]

at this interface, assuming its one-cycle occurrence-transport and lower
compiler/source premises.  This is not an unconditional all-PBBS theorem:
the present opening theorems alone neither create the one-cycle bank nor
improve the additive `m` in (4.11) to an absolute constant.

This is only the strongest dimension-uniform conclusion obtained from
cyclic all-depth support with no positional information.  It is not meant
to supersede better recursive or finite upper bounds elsewhere in the
repository.

## 5. Irreducible unique-witness obstruction

For an owner start `i`, define its forced height

\[
 \lambda_i=max\bigl(\{q:\ U(i,q)\text{ is a required target and }
              (i,q)\text{ is its unique cyclic witness}\}\cup\{0\}\bigr).
\tag{5.1}
\]

Every selected witness bank has

\[
                         h_i\ge\lambda_i.
\tag{5.2}
\]

Consequently every prefix-copy opening obeys the proof-safe lower bound

\[
 \boxed{
 \chi(A,T)\ge
 \min_c\max_{0\le t<u}
       (\lambda_{c-1-t}-t)_+.}
\tag{5.3}
\]

#### Proof

A globally unique target occurrence must be used by every witness selector,
giving (5.2).  Substitute it in (3.3), or directly apply Lemma 1.1 to each
unique occurrence. `square`

Thus `B+1` via cyclic prefix copying requires a cut whose predecessor has
no unique witness above depth one, whose second predecessor has no unique
witness above depth two, and so on.  Hybrid moves can help only by creating
new occurrences or by moving the forced intervals into such a staircase.
Cyclic support by itself says nothing about (5.3).

## 6. What the resident/common-history hybrid does and does not imply

The resident clean-C6 hybrid proves, on the same literal source packet:

1. exact occurrence transport of the strict-lower compiler;
2. positive-run residence; and
3. inclusion of complete **internal cyclic** upper decks of the displayed
   resident port components.

For a target with a witness wholly inside a packet which is disjoint from
the final cut, that witness has overhang zero and contributes nothing to
`K_C(Y)`.  Thus protected internal packets may delete targets from the
opening obstruction.

However, internal deck inclusion has no implication for an interval which
uses an arbitrary exterior context or crosses the final cut.  In
particular it supplies neither

\[
 K_C^{new}(Y)\subseteq K_C^{old}(Y)
\]

at a named exterior cut nor a bound on the new height word.  Such a
conclusion would require one of:

* an occurrence map preserving or decreasing the overhang (1.7);
* regeneration by complete closed resident components until the final
  cut is chosen; or
* a separate protected exterior witness bank.

Therefore the strongest proof-safe synthesis of the two new PBBS results
is:

\[
 \boxed{
 \text{fixed all-depth upper bank}
 +\text{ hybrid lower/internal transport}
 +\text{ bounded height staircase (4.9)}
 \Longrightarrow B(k)+O(1).}
\tag{6.1}
\]

The third conjunct is genuinely still open.  It is the sharp global PBBS
opening gate; it is not another lower Hall or local C6 problem.

On the upper-middle complement face there is an even sharper formulation.
The fixed gap section naturally pairs a lower target occurrence `S` with
the upper occurrence of its complement on the complementary owner block.
The common-history hybrid transports the literal lower source cell, while
its resident theorem preserves internal upper **support**.  Neither theorem
says that these two images remain one paired history.  Support inclusion
cannot be substituted for that occurrence statement when choosing the
final cut.

### Protected quiet-tail fusion lemma (exact missing opening theorem)

It is enough to prove that the complemented PBBS factor admits a serial
resident/common-history rethread with all of the following properties:

1. the transported gap-section strict-lower cells remain valid and
   distinct;
2. every proper upper target has one named terminal owner-interval witness;
3. the terminal factor is one source cycle; and
4. `m-1` consecutive starts immediately before one cut begin none of the
   named upper witnesses.

Under these hypotheses, the standard `d`-letter source unroll preserves
all owners and all lower cells.  Item 4 makes the terminal height word zero
on the preceding `m-1=u` starts, so Theorem 3.1 with `C=0` preserves every
proper upper witness.  The full-ground target is the union of the complete
opened path.  Thus the opening itself has zero additive cost.

The scalar availability required by item 4 is already proved in (4.7):
there are at least `m` eligible height-zero occurrence tokens.  What remains
is solely their paired, owner-legal physical placement.

## 7. Scope summary

Proved here:

1. exact source/owner interval conversion (1.2);
2. exact `C`-letter overhang and truncated target cores;
3. necessary and sufficient prefix-copy opening criterion (2.4);
4. exact selected-bank height-staircase criterion (3.4);
5. an explicit application to the phase-shifted fixed PBBS section;
6. the forced-height obstruction (5.3); and
7. the exact reason the local resident hybrid does not yet imply a global
   opening theorem.

Not proved here:

1. a bounded PBBS staircase defect;
2. a rethreading which orders the fixed-section heights into the required
   terminal staircase;
3. occurrence-level overhang monotonicity for exterior hybrid witnesses;
4. zero-gap residence or common-cap compatibility beyond the imported
   source premises; or
5. `nu(k)<=B(k)+O(1)` unconditionally.

The next theorem should target only one of two equivalent positive forms:

* **height form:** build a terminal owner suffix satisfying (4.9) for
  constant `C`; or
* **core form:** prove that for constant `C`, the union of the truncated
  cores `K_C(Y)` does not cover the final owner cycle.
