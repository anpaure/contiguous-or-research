# Gate C: fractional Hamilton flags and an integral non-GK SCD repair

**Status (2026-08-22).**  Every assertion below is proved.  There is no
marginal fractional obstruction, at the level of individual central flags
and coordinate arcs, to combining exact Boolean flags with the Hamilton
label projection of coherent tours: the uniform fractional flag factor is
simultaneously

1. a convex average of genuine full symmetric-chain decompositions; and
2. an exact fractional sum of directed Hamilton arc-projection bundles,
   not necessarily rankwise target-disjoint.

There is also an integral positive result.  A Catalan-sized family of
pairwise compatible central diamond switches changes the ordered
Greene--Kleitman SCD into a genuine non-GK SCD.  In its central flag arc
multigraph, a subfamily of

\[
 \left({b+1\over2b-1}-o(1)\right)\binom{2b}{b-1}
 =\left({1\over2}+o(1)\right)\binom{2b}{b-1}           \tag{0.1}
\]

flags decomposes into the exact \((b-1)/2\)-fold Hamilton projections
required by coherent tours.

This is an arc-level theorem, not a tour matching.  Flags assigned to one
Hamilton bundle need not have the middle sets or packet order of a coherent
tour.  The result closes the marginal fractional SCD/Hamilton-arc
compatibility question, proves nonzero integral cyclic support inside a
full non-GK SCD, and isolates the remaining problem as the joint
middle-window/FIFO lift.

Throughout,

\[
 n=2b,\qquad b\ge3\text{ is odd},\qquad
 W=\binom{2b}{b},\qquad N=\binom{2b}{b-1}={b\over b+1}W,
 \qquad h={b-1\over2}.                                  \tag{0.2}
\]

Here the Boolean lattice is \(2^\Omega\), where
\(\Omega=\{0,1,\ldots,2b-1\}\).  A saturated chain contains one set in
each consecutive rank from its bottom to its top; it is symmetric when
the two endpoint ranks sum to \(2b\).  A full symmetric-chain
decomposition (SCD) is a partition of \(2^\Omega\) into saturated
symmetric chains.  The *central flag* of a chain crossing ranks
\(b-1,b,b+1\) is its triple at those ranks.

## 1. The complete central-flag orbit

Let \(\mathfrak F\) be the set of all flags

\[
 f=(L,C,U),\qquad L\subset C\subset U,qquad
 (|L|,|C|,|U|)=(b-1,b,b+1).                             \tag{1.1}
\]

Write

\[
 p(f)=C\setminus L,\qquad q(f)=U\setminus C,            \tag{1.2}
\]

so \(f\) has directed coordinate arc \(p(f)\to q(f)\).
Every lower target lies in \(b(b+1)\) flags: choose its first and second
added coordinates in order.  The same holds at the upper rank by
complementation.  Every middle target lies in \(b^2\) flags: choose the
deleted member of the middle set and the added member of its complement.
Consequently

\[
                         |\mathfrak F|=N b(b+1).         \tag{1.3}
\]

Give every flag the weight

\[
                             w={1\over b(b+1)}.          \tag{1.4}
\]

Then every rank-\((b-1)\) and rank-\((b+1)\) target has exact load one,
while every middle target has exact load

\[
                             b^2w={b\over b+1}.          \tag{1.5}
\]

These are precisely the loads of the central flags of a full SCD: all
adjacent targets occur, and the \(W/(b+1)\) singleton middle chains carry
no three-rank flag.

### Theorem 1.1 (the uniform factor is fractionally SCD-realizable)

The weighting (1.4) is a convex average of the integral central flag
factors of genuine full SCDs.

#### Proof

Fix any full SCD, for example an ordered Greene--Kleitman SCD, and take all
of its images under the symmetric group on the \(2b\) coordinates with
equal weight.  Every image has exactly \(N\) disjoint central flags and is
a genuine full SCD.  The symmetric group is transitive on \(\mathfrak F\),
so every flag has the same average weight.  Total flag mass is \(N\), and
(1.3) makes the common weight \(N/|\mathfrak F|=1/[b(b+1)]\), exactly
(1.4). \(\square\)

## 2. Exact fractional Hamilton arc-marginal decomposition

Fix distinct coordinates \(x,y\).  A flag has arc \(x\to y\) precisely
when

\[
 L\in\binom{\Omega\setminus\{x,y\}}{b-1},\qquad
 C=L\cup\{x\},\qquad U=L\cup\{x,y\}.
\]

Thus every ordered arc supports exactly

\[
                         A=\binom{2b-2}{b-1}             \tag{2.1}
\]

flags and has total weight \(Aw\).

Let \(\mathfrak H\) be the set of directed Hamilton cycles on \(\Omega\),
where cyclic rotations of a listing describe the same cycle.  Then

\[
 |\mathfrak H|=(2b-1)!,\qquad
 |\{H\in\mathfrak H:x\to y\in H\}|=(2b-2)!.             \tag{2.2}
\]

Define a joint flag--cycle weight

\[
 z(H,f)=
 \begin{cases}
 \displaystyle {w\over(2b-2)!},&p(f)\to q(f)\in H,\\[5pt]
 0,&\text{otherwise}.
 \end{cases}                                             \tag{2.3}
\]

Summing (2.3) over \(H\) gives \(w\) at every flag by (2.2).  For a fixed
Hamilton cycle \(H\), every one of its arcs receives the same bundle mass

\[
 \theta={Aw\over(2b-2)!}.                                \tag{2.4}
\]

This marginal description can be coupled into \(h\)-fold Hamilton
arc-projection bundles.  For each arc of a fixed \(H\), choose an
\(h\)-subset of its \(A\) supporting flags uniformly, and couple the
choices on the \(2b\) arcs by their product distribution.  Give this
distribution total mass \(\theta/h\).  A particular flag then has
marginal

\[
 {\theta\over h}\,{h\over A}
 ={w\over(2b-2)!}=z(H,f).
\]

Flags selected on different arcs are automatically distinct, since a
flag has a unique directed arc.  They need not, however, be rankwise
target-disjoint inside one bundle: two selected flags can share a lower,
middle, or upper member.  Therefore (2.3) is an exact fractional
decomposition of the SCD-realizable flag factor into distinct-flag sets
whose arc multigraph is \(hH\).  This is precisely the coordinate
multigraph required of a coherent tour, not its target or middle-window
geometry.
The total projected-tour mass is exactly

\[
 {|\mathfrak H|\theta\over h}
 ={N\over b(b-1)},                                       \tag{2.5}
\]

the total flag mass \(N\) divided by the \(b(b-1)\) internal flags in one
tour.

This proves that SCD extendability, rank loads, coordinate-arc balance,
and Hamilton divisibility are perfectly compatible fractionally.  It does
not couple the different arcs of one \(H\) through rankwise-disjoint
targets or common coherent-tour middle geometry.

## 3. Exact central-diamond switches preserve a full SCD

Let \(\mathscr D\) be an arbitrary full SCD.  Let \(M\) be the set of its
middle members whose chains cross ranks \(b-1,b,b+1\), and let
\(Z=\binom{\Omega}{b}\setminus M\) be its singleton middle chains.  Thus

\[
                         |M|=N,\qquad |Z|={W\over b+1}={N\over b}.       \tag{3.1}
\]

For \(C\in M\), write its central flag as \(L_C\subset C\subset U_C\)
and define the other middle vertex of the same Boolean diamond by

\[
 \phi(C)=L_C\cup(U_C\setminus C).                        \tag{3.2}
\]

Replacing \(C\) by \(\phi(C)\) in its chain preserves both adjacent sets
and reverses the coordinate arc:

\[
 p(C)\to q(C)\quad\longmapsto\quad q(C)\to p(C).         \tag{3.3}
\]

### Theorem 3.1 (simultaneous diamond-switch criterion)

For \(S\subseteq M\), simultaneously switch exactly the flags indexed by
\(S\).  This produces another full SCD, changing no set outside the middle
rank and no rank-\((b\pm1)\) incidence, if and only if

\[
 \boxed{
 \phi|_S\text{ is injective},\qquad
 \phi(S)\cap(M\setminus S)=\varnothing.}                 \tag{3.4}
\]

#### Proof

Necessity is immediate: two switched chains cannot acquire the same middle
set, and a switched chain cannot acquire the middle member of an unchanged
chain.

Assume (3.4).  Replace \(C\) by \(\phi(C)\) in every chain indexed by
\(C\in S\).  The new middle members are distinct and avoid every unchanged
middle member.  Remove from the singleton list every member of
\(Z\cap\phi(S)\), and add every member of \(S\setminus\phi(S)\).  Since
\(\phi|_S\) is injective, the removed and added singleton counts agree:

\[
 |Z\cap\phi(S)|=|S\setminus\phi(S)|.
\]

All middle sets are again used exactly once.  Every changed chain remains
saturated and symmetric because only the middle of the same diamond was
exchanged.  All other ranks and chains are unchanged.  Hence the result is
a full SCD. \(\square\)

Theorem 3.1 is an exact integral reduction.  It separates SCD extension
from arc repair: one may reverse a desired flag set precisely when its
alternate-middle map is an injective partial permutation closed away from
the unchanged middle owners.

## 4. A Catalan switch bank in the Greene--Kleitman SCD

Use the ordered Greene--Kleitman SCD on binary words of length \(2b\), with
one denoting membership.  Greedy bracketing pairs a zero with the latest
unpaired one to its left.  After bracketing, all unpaired zeros precede
all unpaired ones.  Fixing the paired positions and bits, and successively
changing the unpaired zeros from right to left into ones, gives one
saturated chain.  These classes partition all binary words.  If there are
\(r\) unpaired positions, the endpoint ranks are \((2b-r)/2\) and
\((2b+r)/2\), so the chain is symmetric.  This is the full ordered
Greene--Kleitman SCD.

A middle word is a singleton chain exactly when it is a Dyck word: every
prefix has at least as many ones as zeros.  Indeed this prefix condition
is exactly the assertion that the balanced word has no unpaired zero,
and then it has no unpaired one either.

For a non-singleton middle word \(C\), its central flag arc is
\(p(C)\to q(C)\), where \(p(C)\) is the leftmost unpaired one and
\(q(C)\) is the rightmost unpaired zero.  Hence \(q(C)<p(C)\), and

\[
 \phi(C)=C-\{p(C)\}+\{q(C)\}.                             \tag{4.1}
\]

The potential \(\sum_{i\in C}i\) strictly decreases under \(\phi\).
Consequently the switch graph has no directed cycles; the admissible
systems in (3.4) are vertex-disjoint directed paths ending at singleton
Dyck words.  The following length-one bank is enough for a positive cyclic
factor.

Put

\[
                         K=\operatorname{Cat}_{b-1}
 ={1\over b}\binom{2b-2}{b-1}.                            \tag{4.2}
\]

A primitive Dyck word has the form \(D=1D'0\), where \(D'\) is an arbitrary
Dyck word of length \(2b-2\); there are exactly \(K\) of them.  Define

\[
                         C_D=0D'1.                        \tag{4.3}
\]

In \(C_D\), the first zero and final one are the only unpaired coordinates;
all of \(D'\) brackets internally.  Thus its GK flag has

\[
 q(C_D)=0,qquad p(C_D)=2b-1,qquad \phi(C_D)=D.           \tag{4.4}
\]

The targets \(D\) are distinct singleton chains, so Theorem 3.1 permits all
\(K\) switches (4.3) simultaneously.  Denote the resulting genuine full
SCD by \(\mathscr D^*\).  Its central arc multigraph contains \(K\) copies
of the ascent \(0\to2b-1\).

We also need the descending path.  The following standard last-minimum
count is included for completeness.

### Lemma 4.1 (uniform consecutive-arc count)

For every \(1\le j\le2b-1\), the ordered GK central flag factor contains
exactly \(K\) flags with arc \(j\to j-1\).

#### Proof

View a middle word as a balanced walk with a one-step \(+1\) and a
zero-step \(-1\).  Its unpaired zeros are exactly the down-steps which
reach a new strict prefix minimum.  Its leftmost unpaired one is the
up-step immediately following the last visit to the global minimum.
Consequently \(q=j-1\) and \(p=j\) exactly when the walk has a unique
global-minimum vertex between steps \(j-1\) and \(j\).

Write such a word uniquely as

\[
                              A\,0\,1\,B,
 \qquad |A|=j-1,\quad |B|=2b-j-1.                       \tag{4.10}
\]

Starting just after the unique minimum, its cyclic step sequence is
\(1BA0\).  This is a primitive Dyck word, so deleting its first and last
steps gives the Dyck word \(D=BA\) of length \(2b-2\).  Conversely, split
any such Dyck word uniquely as \(D=BA\) with the lengths in (4.10), and
form \(A01B\).  Cyclically starting after its displayed zero gives
\(1D0\), which is primitive Dyck; hence the displayed valley is its unique
global minimum and its two steps are precisely \(q,p\).  The two maps are
inverse, so the required number is
\(\operatorname{Cat}_{b-1}=K\). \(\square\)

### Theorem 4.2 (an integral Hamilton-projection subsystem)

The genuine full SCD \(\mathscr D^*\) contains
\(T_*=\lfloor K/h\rfloor\) pairwise rankwise-target-disjoint subsystems,
each having arc multigraph \(hH_*\) for one directed Hamilton cycle
\(H_*\).  Their union contains a \((1/2+o(1))\)-fraction of all \(N\)
central flags.

#### Proof

None of the switches (4.3) changes a consecutive descending arc.  Combining
(4.4) and Lemma 4.1, \(\mathscr D^*\) contains the directed Hamilton cycle

\[
 H_*:\quad
 0\to2b-1\to2b-2\to\cdots\to1\to0                       \tag{4.5}
\]

with multiplicity exactly \(K\).  Partition the flags on each edge of
\(H_*\) into common groups of \(h\), discarding fewer than \(h\) flags per
edge.  This gives

\[
 T_* =\left\lfloor{K\over h}\right\rfloor               \tag{4.6}
\]

disjoint exact \(h\)-fold Hamilton projection bundles, containing

\[
 R_*=b(b-1)T_*                                           \tag{4.7}
\]

central flags.  Since

\[
 {2bK\over N}={b+1\over2b-1},                            \tag{4.8}
\]

we obtain

\[
 \boxed{
 {R_*\over N}\ge {b+1\over2b-1}-{b(b-1)\over N}
 ={1\over2}+{3\over2(2b-1)}-{b(b-1)\over N}
 ={1\over2}+\Theta(b^{-1}).}                            \tag{4.9}
\]

Thus a genuine full non-GK SCD has an integral fixed-fraction central flag
subsystem satisfying exactly the coordinate-Hamilton multiplicities of
coherent tours. \(\square\)

## 5. Two canonical tour phases have one defect per packet

The arc bundles in Theorem 4.2 are not arbitrary noise: two actual
coherent tour phases are locally very close to \(\mathscr D^*\).  The following
explicit form makes both the positive statement and its limitation exact.
All coordinate arithmetic in this section is modulo \(n=2b\).  For a
phase \(\delta\in\{0,1\}\), put

\[
 I(r)=\{r,r+1,\ldots,r+b\},\qquad
 a_s^\delta=\delta+(s+1)(b-1)\quad(0\le s<b),           \tag{5.1}
\]

and define the \(b+1\) windows of packet \(s\) by

\[
 W^\delta_{s,t}=I(a_s^\delta-t+1)\setminus\{a_s^\delta+1\},
 \qquad 0\le t\le b.                                    \tag{5.2}
\]

Since \(a^\delta_{s+1}=a^\delta_s+b-1\), including cyclically at
\(s=b-1\), \(W^\delta_{s,b}=W^\delta_{s+1,0}\).  Consecutive windows differ by one FIFO
replacement.  Pair coordinate \(j\) with \(j+b\).  The boundary windows
\(W^\delta_{s,0}\) are transversals of these antipodal pairs.  For
\(1\le t\le b-1\), the internal window \(W^\delta_{s,t}\) doubles the pair of
\(a^\delta_s-t+1\), empties the pair of \(a^\delta_s+1\), and meets every
other pair once.  Indeed the empty-pair label is
\(\delta-s\pmod b\), while the double-pair label is smaller by \(t\);
the ordered labels are therefore all distinct.  Thus, for each
\(\delta\), (5.2) is a FIFO-closed coherent \(b\)-packet tour.

Write its internal flag as

\[
 \begin{aligned}
 r^\delta_{s,t}&=a^\delta_s-t+1,\\
 C^\delta_{s,t}&=W^\delta_{s,t}
      =I(r^\delta_{s,t})\setminus\{r^\delta_{s,t}+t\},\\
 L^\delta_{s,t}&=C^\delta_{s,t}\setminus\{r^\delta_{s,t}\},\\
 U^\delta_{s,t}&=C^\delta_{s,t}\cup\{r^\delta_{s,t}-1\}.
 \end{aligned}                                          \tag{5.3}
\]

Its coordinate arc is \(r^\delta_{s,t}\to r^\delta_{s,t}-1\).  Since
\(\gcd((b-1)/2,b)=1\), the values \(a^\delta_s\) run through all residues
of parity \(\delta\).  Among \(t-1=0,\ldots,b-2\) there are \(h\) shifts
of each parity.  Hence every arc of \(H_*\) occurs exactly \(h\) times,
as required.

### Theorem 5.1 (two exact \(q-b\) overlaps)

Let \(\mathfrak F^*\) be the central flag factor of \(\mathscr D^*\), and
let \(\mathcal T^\delta_*\) be either coherent phase tour (5.2).  Then

\[
 F^\delta_{s,t}:=(L^\delta_{s,t},C^\delta_{s,t},U^\delta_{s,t})
 \in\mathfrak F^*
 \quad\Longleftrightarrow\quad 2\le t\le b-1.            \tag{5.4}
\]

Consequently

\[
 |\mathcal T^\delta_*\cap\mathfrak F^*|
 =b(b-2)=b(b-1)-b.                                      \tag{5.5}
\]

The unique missing flag in packet \(s\) is explicitly

\[
 \left(
 C^\delta_{s,1}\setminus\{a^\delta_s\},\
 I(a^\delta_s)\setminus\{a^\delta_s+1\},\
 C^\delta_{s,1}\cup\{a^\delta_s-1\}
 \right).                                               \tag{5.6}
\]

The retained flag sets for \(\delta=0\) and \(\delta=1\) are jointly
rankwise-target-disjoint.

#### Proof

Read the membership word of \(C^\delta_{s,t}\) starting at coordinate
\(r=r^\delta_{s,t}\) and proceeding in increasing cyclic coordinate order.
Equation (5.3) gives, independently of \(s\),

\[
 \rho_r(C^\delta_{s,t})
 =1^t\,0\,1^{\,b-t}\,0^{\,b-1}.                         \tag{5.7}
\]

For \(t\ge2\), (5.7) is primitive Dyck: its height stays positive until
its final symbol.  If \(r\ne0\), the ordinary balanced walk of
\(C^\delta_{s,t}\) therefore has its unique global minimum at the boundary
between coordinates \(r-1,r\).  By the last-minimum characterization in
Lemma 4.1, its GK central flag has \(p=r,q=r-1\), hence is exactly
\(F^\delta_{s,t}\).  This flag was not switched in constructing
\(\mathscr D^*\), because its arc is not \((2b-1)\to0\).

If \(r=0\), then \(C^\delta_{s,t}\) itself is the primitive Dyck word
\(D=1D'0\).  Its switched source is \(0D'1\); the latter has lower member
\(D\setminus\{0\}=L^\delta_{s,t}\) and upper member
\(D\cup\{2b-1\}=U^\delta_{s,t}\).  Thus the new flag in
\(\mathscr D^*\) is again exactly \(F^\delta_{s,t}\).

For \(t=1\), (5.7) returns to height zero after its first two symbols, so
it is not primitive and the proposed boundary is not a unique cyclic
minimum.  If \(r\ne0\), the GK predecessor/successor therefore do not
give the desired arc \(r\to r-1\); the only new flags of
\(\mathscr D^*\) have arc \(0\to2b-1\).  If \(r=0\), the word is a
nonprimitive singleton Dyck word and was not one of the switched targets.
Hence \(F^\delta_{s,1}\notin\mathfrak F^*\) in every packet, proving
(5.4)--(5.6).

Finally, a retained flag determines its arc start \(r\) and, inside the
cyclic interval \(I(r)\), the unique omitted coordinate \(r+t\).  It
therefore determines \(a^\delta_s=r+t-1\), whose parity is \(\delta\).
The two retained phase systems are disjoint.  Both lie in the single
central factor \(\mathfrak F^*\); distinct flags of that factor have
distinct lower targets, distinct used middle targets, and distinct upper
targets.  Their union is therefore rankwise-target-disjoint. \(\square\)

### Corollary 5.2 (the deletion is locally negligible, not a packing)

Deleting the \(b\) flags (5.6) leaves a rankwise-target-disjoint partial
tour of size \(q-b=b(b-2)\).  Its relative loss is

\[
                         {b\over q}={1\over b-1}=o(1).   \tag{5.8}
\]

Thus, *if* one could pack \(T=(1+o(1))N/q\) such partial tours in a
single SCD and repair \(O(b)\) packet defects per tour, the total repair
budget would be

\[
                         O(bT)=O(N/b)=o(N),              \tag{5.9}
\]

which is compatible with a coefficient-one count.  This is only a
numerical compatibility statement: (5.9) is not a connector or deeper
chain construction.

Moreover the fixed cycle \(H_*\) supplies exactly the two phase supports
in Theorem 5.1, not a growing family.  Indeed a directed Hamilton cycle
\(H=(h_0,\ldots,h_{2b-1})\) forces the antipodal pairing
\(\{h_j,h_{j+b}\}\).  Relabelling the canonical tour by
\(2j\mapsto h_j,\ 2j+1\mapsto h_{j+b}\) fixes one support.  Even rotations
of the listing merely change its packet origin, while odd rotations give
the other phase; there are no further choices.  Reusing \(H_*\) therefore
reuses one of the same two retained flag sets.  Together the two partial
tours in Theorem 5.1 cover only \(2b(b-2)=O(b^2)=o(N)\) flags, despite the
many abstract arc bundles in Theorem 4.2.

There is also an exact scarcity benchmark.  For any fixed central factor
\(\mathfrak A\) of \(N\) flags, average over both phase supports of all
\((2b-1)!\) directed Hamilton cycles.  The symmetric group is transitive
on the complete flag set \(\mathfrak F\), every support has
\(q=b(b-1)\) flags, and \(|\mathfrak F|=Nb(b+1)\).  Hence

\[
 {1\over2(2b-1)!}\sum_{H,\delta}
      |\mathcal T^\delta(H)\cap\mathfrak A|
 ={Nq\over|\mathfrak F|}
 ={b-1\over b+1}<1.                                    \tag{5.10}
\]

Thus the overlap (5.5) is extremely atypical.  In the canonical rooted
phase convention used by the finite checker, exact enumeration gives, for
\(b=3\), maximum overlap \(3/6\), attained by four cycles.  For \(b=5\),
\(H_*\) is the unique cycle with the maximum overlap \(15/20\); the next
maximum is \(11/20\), attained by eighteen cycles.  These finite facts do
not prove asymptotic scarcity, but they rule out interpreting the
canonical near-tour as an already available large packing.

## 6. Exact remaining lift

The construction proves three facts which were previously conflated:

* full SCD extension and Hamilton-balanced central flags are marginally
  compatible;
* this marginal compatibility is exact fractionally on all central flags;
  and
* it is integral on a \((1/2+o(1))\)-fraction of one explicit full SCD.

It does **not** prove that the \(2b\) arc classes in one bundle can be
matched so that their middle sets are the \(b(b-1)\) defect-one windows of
one coherent tour.  Arbitrarily grouping \(h\) flags of each arc loses the
pairing, cyclic-order, initial-state, and packet-boundary correlations.
Nor does the central diamond switch say that deeper members of the switched
SCD chains are literal windows of that tour.

The remaining integral question can now be stated without an abstract SCD
or coordinate-balance ambiguity:

> Starting from the explicit non-GK SCD \(\mathscr D^*\), can one select
> \((1-o(1))N/[b(b-1)]\) coherent tours whose internal flags are distinct
> members of its central factor, possibly after further switch systems
> satisfying (3.4), while changing only \(o(N)\) deeper chain assignments?

The fixed Hamilton cycle \(H_*\) alone supplies only the projected capacity
in (4.9); achieving coefficient one must mix further Hamilton projections
or use a recursive residual construction.  The middle-window coinstantiation,
not fractional SCD extendability, is the live obstruction.

## 7. Finite audit

The companion checker

`scratch/verify_gate_c_non_gk_scd_hamilton_flag_repair_20260822.py`

enumerates the ordered GK chains and central flags for \(2\le b\le10\),
verifies Theorem 3.1 on the Catalan switch bank, checks the primitive-Dyck
bijection (4.3)--(4.4), the consecutive-arc count, the full SCD after all
simultaneous switches, and the Hamilton multiplicity and ratios
(4.5)--(4.9).  It also checks all fractional incidence identities through
\(b=30\), and verifies the two phase tours, every window/flag formula in
Section 5, the exact \(q-b\) overlaps, and joint rankwise disjointness
through every odd \(3\le b\le101\).

The independent exploratory checker

`scratch/research_gate_c_tour_scd_overlap_spectrum_20260822.py`

enumerates the rooted-phase overlap spectrum exactly for \(b=3,5\),
verifies the mean (5.10) in that convention, and performs a fixed-seed
\(b=7\) sample.  The checkers are confirmatory; all general proofs are
contained above.
