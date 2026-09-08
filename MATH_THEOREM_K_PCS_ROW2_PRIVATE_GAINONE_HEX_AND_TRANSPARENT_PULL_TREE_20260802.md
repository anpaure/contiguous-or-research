# `PCS` Row 2: private gain-one hex absorbers and the transparent pull-tree gate

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot / immediate-upper availability  
**Status:** unconditional odd-host absorber catalogue and private-packing
theorem; exact prospective composition; no all-parameter `PCS`, fixed-factor
repair, residence, deep-upper, compiler, or regeneration claim

## 0. Outcome

Row 2 of `PCS(m,d)` asks for more than an abstract upper-colour Hall
matching.  Relative to a fixed predecessor matching `M_0`, an upper colour
has only `m+1` rooted occurrences, not `binom(m+1,2)`: choosing the corner
of its Boolean diamond is already correlated with `M_0`.  The protected
rooted-tail theorem closes the upper-colour/tail projection, but it does not
make the other heads distinct and it does not produce a path or cycle.

This note proves a different, prospective bounded-defect statement.  On the
odd host `[2m-1]`, every prescribed diamond atom has a fixed-slot canonical
subcatalogue of exactly

\[
                    2(m-1)(m-2)                              \tag{0.1}
\]

literal gain-one suspended-hex packets.  Apart from the four resources of
the prescribed atom, every named lower, upper, or owner-slot resource lies
in at most

\[
                           2(m-1)                              \tag{0.2}
\]

of those packets.  Consequently, `p` pairwise-resource-disjoint prescribed
atoms admit pairwise-private packets avoiding an external protected bank
`B` whenever

\[
                    |B|+12(p-1)<m-2.                           \tag{0.3}
\]

The result treats every rank-`(m+1)` colour alike.  In particular, the
boundary/`D` colours omitted by a restricted quotient audit receive the same
catalogue as every other member of the full immediate-upper shore.

The packets are **prospective gain-one absorbers**, not post-hoc toggles of
an arbitrary two-factor.  Their two-edge off phases must be planted in a
defect-aligned partial forest, with the four target resources left free.
Turning them on preserves every old named resource and adds exactly the
target lower colour, upper colour, and two owner slots.  A separate graphic
condition is still needed to make the resulting support a forest or cycle
cover.  A protected palette-neutral pull tree can then merge its components.

Thus (0.3) proves the quantitative Boolean supply/packing part of a Row-2
absorber for every regime `p+|B|=o(m)`, in particular for `O(d)` banks with
`d=O(sqrt(m))`.  The exact remaining lemma is the prospective planting of
the off phases together with a graphic-safe target-slot assignment and a
surviving aperture-compatible pull tree.  This is strictly smaller than
`PCS`: it contains no source chronology, residence, higher-shadow, preword,
or compiler row.

## 1. Odd-host diamond atoms

Assume `m>=3` and put

\[
              \Omega=[2m-1],\qquad r=m-1.                       \tag{1.1}
\]

A literal diamond atom is

\[
 A=(D,V;\xi_{D+p},\xi_{D+q}),\qquad
 |D|=r,\quad V=D+p+q,                                          \tag{1.2}
\]

where `p,q notin D` are distinct and the two displayed symbols are the
chosen slots at the two rank-`m` owners.  Its four named resources are

\[
                 D,\quad V,\quad \xi_{D+p},\quad \xi_{D+q}.     \tag{1.3}
\]

Choose

\[
 b\in D,\qquad c\in\Omega\setminus V,\qquad
 (a,s)\in\{(p,q),(q,p)\},\qquad K=D-b.                         \tag{1.4}
\]

Define three lower colours

\[
 D_a=K+a,\qquad D_b=K+b=D,\qquad D_c=K+c,                      \tag{1.5}
\]

three upper colours

\[
 U_{abs}=K+a+b+s=V,\qquad
 U_{acs}=K+a+c+s=V-b+c,\qquad
 U_{bcs}=K+b+c+s=D+c+s,                                      \tag{1.6}
\]

and the six rank-`m` owners

\[
                         X_{uv}=K+u+v.                         \tag{1.7}
\]

Fix in advance one canonical literal slot `xi_X` at every possible
auxiliary owner `X` in the catalogue, and retain the prescribed target
slots at `X_ab=D+a` and `X_bs=D+s`.  This fixed slot section is part of the
packet definition; slots are not re-chosen separately for different
catalogue members.  Write

\[
\begin{array}{lll}
 e_a=(D_a,U_{acs};\xi_{ac},\xi_{as}),&&
 e_b=(D_b,U_{abs};\xi_{ab},\xi_{bs})=A,\\
 e_c=(D_c,U_{bcs};\xi_{bc},\xi_{cs}),
\end{array}                                                   \tag{1.8}
\]

and

\[
\begin{array}{lll}
 f_a=(D_a,U_{abs};\xi_{ab},\xi_{as}),&&
 f_b=(D_b,U_{bcs};\xi_{bc},\xi_{bs}),\\
 f_c=(D_c,U_{acs};\xi_{ac},\xi_{cs}).
\end{array}                                                   \tag{1.9}
\]

Every displayed containment is literal.  All resources are occurrence
labelled; two equal owner masks with different slots are different slot
resources.

### Lemma 1.1 (gain-one resource identity)

Put

\[
          Z^{\rm off}=\{e_a,e_c\},\qquad
          Z^{\rm on}=\{f_a,f_b,f_c\}.                          \tag{1.10}
\]

Then

\[
 \operatorname{res}(Z^{\rm on})
   =\operatorname{res}(Z^{\rm off})
       \mathbin{\dot\cup}\operatorname{res}(A)                \tag{1.11}
\]

as multisets of lower colours, upper colours, and owner slots.  Each phase
is a physical matching and a three-edge or two-edge forest on its displayed
owners.

#### Proof

The off phase uses lower resources `D_a,D_c`, upper resources
`U_acs,U_bcs`, and slots `xi_ac,xi_as,xi_bc,xi_cs`.  The on phase uses the
same eight resources and additionally `D_b,U_abs,xi_ab,xi_bs`, which are
exactly (1.3).  Within each resource type the displayed sets are distinct:
the fresh coordinate `c`, the removed coordinate `b`, and the two-element
bank `{p,q}` recover their roles.  Hence both phases are matchings and
(1.11) follows.  Their physical edges have distinct displayed owner slots,
so each local projection is a forest.  \(\square\)

The final sentence is local.  Replacing the off phase inside a larger
forest can still make a global cycle; Section 4 retains that graphic row.
Also, the literal edge `e_b=A` is a bookkeeping ticket, not an on-phase
edge: the four resources of `A` are distributed among `f_a,f_b,f_c`.
In particular the new occurrence of the target upper `V` is `f_a`.
Therefore a later fixed-`M_0` audit must test the tail/head of `f_a`; it may
not reuse the endpoints of `e_b` by name.

## 2. Exact catalogue size and resource loads

### Theorem 2.1 (canonical odd-host target catalogue)

For every target atom `A` in (1.2), the choices (1.4), under the fixed slot
section of Section 1, give exactly

\[
                              2r(r-1)                           \tag{2.1}
\]

distinct gain-one packets.  If `rho` is any named resource other than the
four target resources (1.3), then at most `2r` packets in the catalogue use
`rho`.

#### Proof

There are `r` choices of `b`, `r-1` choices of `c`, and two orientations.
The target `D,V` recovers the fixed bank `{p,q}`.  Among the two auxiliary
lower resources, `D_a` is the unique one containing one member of `{p,q}`,
whereas `D_c` contains neither.  Thus `D_a` recovers `a` and the
orientation, `D-D_a` recovers `b`, and `D_c-D` recovers `c`.  Hence
different triples in (1.4) give different packet supports.

For completeness, the following table lists every non-target resource.
The last column is its maximum multiplicity in the target catalogue.

\[
\begin{array}{c|c|c}
\text{resource}&\text{mask}&\text{maximum load}\\ \hline
D_a&D-b+a&r-1\\
D_c&D-b+c&2\\
U_{acs}&V-b+c&2\\
U_{bcs}&D+c+s&r\\
X_{ac}&D-b+a+c&1\\
X_{as}&V-b&2(r-1)\\
X_{bc}&D+c&2r\\
X_{cs}&D-b+c+s&1
\end{array}                                                   \tag{2.2}
\]

For example, fixing `X_bc=D+c` fixes `c`, while `b` and the orientation
remain free, giving `2r`, the largest entry.  Fixing `X_as=V-b` fixes `b`,
while `c` and the orientation remain free, giving `2(r-1)`.  The other
entries follow by the same literal recovery.  A fixed owner-slot resource
has load no larger than its owner mask.  The target owners `D+p,D+q`, the
target lower `D`, and target upper `V` are excluded because every packet is
supposed to use those four resources.  This proves (2.1)--(2.2).  \(\square\)

This is an occurrence-level load bound for the fixed-slot canonical
subcatalogue.  It does not count only masks and then silently identify
incompatible slots.  Additional legal slot lifts, when present, are not
part of the exact count (2.1).

## 3. A deterministic private-packing theorem

Call targets `A_1,...,A_p` **resource-disjoint** when their lower colours,
upper colours, and two owner-slot resources are pairwise distinct.  Let `B`
be an external bank of named resources disjoint from every target.

### Theorem 3.1 (private gain-one packing)

If

\[
                         |B|+12(p-1)<r-1,                       \tag{3.1}
\]

then one can choose a gain-one packet `Z_i` for every target `A_i` such
that

1. `Z_i` avoids `B`;
2. `Z_i` meets the target-resource bank only in the four resources of
   `A_i`; and
3. the eight auxiliary resources of distinct packets are pairwise
   disjoint.

Equivalently, the complete twelve-resource packet supports are pairwise
disjoint.

#### Proof

Choose the packets greedily.  When choosing the packet for `A_i`, forbid:

* the external bank `B`;
* the four resources of each of the other `p-1` targets; and
* the eight auxiliary resources of every packet already chosen.

At every step the number of forbidden non-target resources is at most

\[
                    |B|+4(p-1)+8(p-1)=|B|+12(p-1).              \tag{3.2}
\]

By Theorem 2.1 each forbids at most `2r` members of the current target
catalogue.  Thus fewer than

\[
          2r(r-1)=|\mathcal Z(A_i)|                              \tag{3.3}
\]

candidates are killed under (3.1), and one remains.  Induction proves all
three assertions.  \(\square\)

### Corollary 3.2 (asymptotic `O(d)` bank)

If `p<=c_1 d`, `|B|<=c_2 d`, and

\[
                    (c_2+12c_1)d<m-2,                           \tag{3.4}
\]

then the whole bank has private packets.  Consequently every fixed-constant
`c_1,c_2` is eventually admissible when `d=O(sqrt(m))`.

The constants are deliberately literal rather than asymptotic.  They can
be improved by exploiting resource types, but (3.1) is already enough to
separate packet abundance from the remaining topology problem.

## 4. Exact prospective absorption

Let `H^-` be an occurrence-labelled partial atom set containing the pivot
collar and all off phases `Z_i^off`.  Assume:

1. `H^-` is a matching in the lower/upper/owner-slot resource host;
2. the four resources of every target `A_i` are unused by `H^-`;
3. every required immediate-upper colour outside
   `{up(A_1),...,up(A_p)}` already has a retained occurrence in `H^-`; and
4. the target uppers are precisely the missing members of the **full**
   immediate-upper shore, including any boundary/`D` members.

Define

\[
 H^+=\left(H^-\setminus\bigcup_i Z_i^{\rm off}\right)
              \cup\bigcup_i Z_i^{\rm on}.                     \tag{4.1}
\]

### Theorem 4.1 (lossless full-shore absorption)

Under Theorem 3.1 and hypotheses 1--4, `H^+` is again a resource matching.
It preserves every named lower, upper, and owner-slot resource used by
`H^-`, and it additionally uses exactly the four resources of every target.
In particular every member of the full immediate-upper shore has an
eligible occurrence in `H^+`.

#### Proof

Sum (1.11) over the pairwise-private packets.  Every old resource cancels
literally and every target resource is added once.  Privacy prevents a
cross-packet collision, and target-resource disjointness prevents a target
collision.  The upper-coordinate assertion is the upper component of the
same identity.  \(\square\)

The theorem proves occurrence availability before any contracted
graphic--Rado selection is invoked.  Once `H^+` is bound to one fixed
predecessor phase and source replay, the protected graphic--Rado theorem
may select one occurrence of every upper colour exactly under its contracted
rank inequalities.  Those inequalities cannot be used to manufacture a
missing family.

### The graphic-ear row

Theorem 4.1 does not say that the rooted projection of `H^+` is acyclic.
The exact additional row is

\[
 r_{M_{\rm gr}}
  \left(\lambda(H^-\setminus\textstyle\bigcup_i Z_i^{\rm off})
       \cup\lambda(\textstyle\bigcup_i Z_i^{\rm on})\right)
 =|H^+|,                                                       \tag{4.2}
\]

when a forest is required, or the corresponding degree-two component
ledger when a cycle cover is required.  Local foresthood in Lemma 1.1 does
not imply (4.2).  This is the first unproved correlation left by the private
packing theorem.

## 5. Transparent pull-tree completion

Suppose the result of Section 4 is completed to a lower-rainbow,
upper-exact cycle cover `F^+` containing the pivot collar.  A pull is called
**Row-2 transparent** when its literal alternating toggle

1. preserves the complete lower- and immediate-upper-colour multisets;
2. preserves the chosen occurrence matching, or supplies an explicit
   colour-preserving bijection between destroyed and new representatives;
3. avoids the pivot collar, every private packet, and the protected opening;
4. is accepted in the same fixed predecessor phase; and
5. when used as an auxiliary component edge, merges the certified two
   components without splitting a third.

A family is **tree-coherent** when a parent-before-child spanning-tree order
keeps every later pull available.  Disjoint mutable supports are a
sufficient, not necessary, certificate.

### Theorem 5.1 (private absorption plus pull tree)

If (4.2) or the declared cycle-cover ledger holds, and the Row-2 transparent
pull auxiliary graph of `F^+` has a tree-coherent spanning tree after the
private packet/protected bank is deleted, then the corresponding pulls give
one lower-rainbow, upper-exact Hamilton cycle containing the pivot collar.
If a protected redundant-provider cut survives, lies outside the collar,
and its omitted root is contained in the intended endpoint owner, deleting
it gives the corrected rooted Hamilton path required in Row 2.

#### Proof

Every pull preserves both palettes and the protected bank.  In the
tree-coherent order each pull merges the current parent aggregate with one
fresh child, so the component number falls by one.  A spanning tree leaves
one cycle.  The protected cut deletes a repeated upper provider, hence no
upper colour, and the explicit containment hypothesis is exactly the
corrected endpoint-aperture condition.  \(\square\)

For a quantitative deletion test, if the unprotected pull auxiliary graph
is `lambda`-edge-connected and every protected or packet resource deletes at
most `L` auxiliary edges, connectivity survives whenever

\[
                  \lambda>L\bigl(|B|+12p\bigr).                 \tag{5.1}
\]

Tree coherence and the endpoint aperture still have to be certified; (5.1)
is only the ordinary cut-survival row.

## 6. The strictly smaller remaining lemma

The new unconditional theorem removes **formal packet supply** and
**resource-private packing** from the prospective Row-2 problem whenever
(3.1) holds.  What remains is the following exact clause.

> **Defect-aligned off-phase/pull lemma `DOP(m,d,p)`.**  Prospectively build
> one fixed-phase lower-rainbow partial forest/cycle cover containing the
> pivot collar and `p` private off phases, with the corresponding target
> lower colours and owner slots free, so that (i) the targets are precisely
> its full-shore upper defects, (ii) the on state passes (4.2) or the exact
> cycle-cover ledger, and (iii) the surviving Row-2-transparent auxiliary
> graph has a tree-coherent spanning tree and a corrected protected cut.

`DOP` plus Theorems 3.1--5.1 proves Row 2 for a `p`-defect controlled-leave
support.  It is strictly smaller than Row 2 itself: the target packets and
their resource privacy are explicit and automatic, while only their
correlated birth inside one graphic support and its neutral gluing tree
remain.

The fixed-`M_0` head collision is not hidden.  The old rooted-tail Hall
theorem gives distinct tails but can repeat the other owners.  `DOP` must
plant the target slots and predecessor phase jointly; separate tail and head
Hall projections are insufficient by the standard even-parity
three-partition obstruction.

## 7. Scope and finite calibration

Unconditional here:

* the literal odd-host gain-one identity;
* the exact fixed-slot canonical catalogue `2(m-1)(m-2)`;
* the exact maximum non-target resource load `2(m-1)`;
* deterministic private packing under (3.1); and
* lossless full-shore absorption once the off phases are planted.

Conditional:

* the global graphic-ear/cycle-cover row;
* the transparent pull-tree and protected opening; and
* fixed-phase/source binding.

Open and not claimed:

* `DOP(m,d,p)` or Row 2 for all parameters;
* a bounded-defect theorem for the standard MMM factor;
* residence, arbitrary-width upper witnesses, the pre-insertion chronology,
  common-cap/compiler assignment, regeneration, or `PCS/PCPS`;
* any `k=17` word or support completion.

At `k=17` one has `m=9`, so the asymptotic inequality (3.1) is not a
certificate for the 22 boundary tickets or for the one-hole trajectory.
Those finite models remain calibration only and require their independent
literal replay and the full-shore support audit.
