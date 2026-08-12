# Ballot-forced cores, the full-factor alternation correction, and a dense suffix \(C_8\) bank

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result

Section 3.6 of
`MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md` correctly
counts

\[
 Z_r={r(r-1)\over r+2}\operatorname {Cat}_r                 \tag{0.1}
\]

ballot-eligible \((r-1)\)-cores. Its next implication needs a correction.
A directed cycle in the functional digraph of the outgoing matching need
not be alternating in the **full** Chung--Feller path factor: a proposed
new half-edge may already be the selected incoming edge of the factor.

There is an exact phase-labelled criterion. If the states on such a
functional cycle have Chung--Feller labels \((P_i,t_i)\), then the lifted
incidence cycle is factor-alternating if and only if the roots \(P_i\) are
pairwise distinct. Thus every admissible cycle furnished by the outgoing
matching is clean. In particular, this bank contains no folded-\(C_6\)
router; folded routers require a cycle using both matching orientations.

The correction does not destroy positive-density supply in the abstract
path ledger. For every
\(r\ge3\), the canonical factor contains an explicit family of

\[
                         \boxed{\operatorname {Cat}_{r-3}}            \tag{0.2}
\]

pairwise vertex-disjoint, ballot-eligible, clean star-\(C_8\) incidence
switches in the abstract path ledger. They affect exactly

\[
 \boxed{
 4\operatorname {Cat}_{r-3}
 =\frac{r(r-1)(r+1)}
 {2(2r-1)(2r-3)(2r-5)}\operatorname {Cat}_r
 =\left(\frac1{16}+O(r^{-1})\right)\operatorname {Cat}_r.}           \tag{0.3}
\]

All selected vertices lie in phases \(r-3,r-2,r-1\). Hence the whole bank
avoids every protected initial phase prefix \(0,\ldots,h-1\) whenever
\(h\le r-3\).

The four cut phases of one switch are \((r-3,r-1,r-2,r-3)\). The toggle is
strand-admissible in the abstract path ledger and has a four-cycle endpoint
action, but its four new row semilengths are

\[
                         r,\quad r+2,\quad r-1,\quad r-1.           \tag{0.4}
\]

Their orbit sum is \(4r\). Thus the bank passes the abstract strand ledger,
the scalar count, and the formal orbit-length equation. It does **not**
pass the physical packet-realizability gate.

Indeed, a nonidentity twist is impossible in an ordinary fixed-exterior
\(r\)-step wreath slab. More sharply, the four port displacements of this
switch are \(1,1,1,2\), so there is no single exterior motion
\(e=|O_L\setminus O_R|\) satisfying

\[
                         e=|P\setminus\tau(P)|                       \tag{0.5}
\]

on all four strands. Even the actual variable row lengths in (0.4) would
require the incompatible exterior motions \(1,3,0,1\). The bank is
therefore only an abstract \(b\)-factor/path-ledger supply theorem unless
one constructs a larger row-dependent boundary-moving packet with every
crossing collar owned exactly.

## 1. The outgoing functional graph and the missing condition

Let \(F\) be the canonical Chung--Feller path factor on

\[
 \mathcal X=\binom{[2r]}r,
 \qquad
 \mathcal Y=\binom{[2r]}{r+1}.
\]

Orient each path from its Dyck root to its complementary terminal state.
Write its two incidence matchings as

\[
 M^\uparrow=\{X_t(P)Y_t(P):0\le t<r\},
 \qquad
 M^\downarrow=\{Y_t(P)X_{t+1}(P):0\le t<r\}.           \tag{1.1}
\]

Fix an \((r-1)\)-set \(K\). Whenever \(K+a\) is not a terminal port, its
unique outgoing edge has the form

\[
                 K+a\longrightarrow K+a+b.                         \tag{1.2}
\]

Draw the arc \(a\to b\). Distinct arcs cannot use the same unordered pair,
because that would repeat the upper vertex \(K+a+b\) in \(M^\uparrow\).

Suppose

\[
                         a_0\to a_1\to\cdots\to a_{\ell-1}\to a_0   \tag{1.3}
\]

is a directed cycle. Put

\[
 X_i=K+a_i,
 \qquad
 Y_i=K+a_i+a_{i+1},                                    \tag{1.4}
\]

with cyclic indices. Its outgoing edges \(X_iY_i\) belong to
\(M^\uparrow\). To be an alternating cycle of the full factor, however,
one also needs

\[
                         Y_iX_{i+1}\notin M^\downarrow
                         \qquad(0\le i<\ell).          \tag{1.5}
\]

Condition (1.5) is absent from the original formulation of Theorem 3.6.

### Proposition 1.1 (exact phase/strand criterion)

Give every nonterminal state its canonical label

\[
                         X_i=X_{t_i}(P_i).             \tag{1.6}
\]

For a directed cycle (1.3), the following are equivalent.

1. Its lift (1.4) is \(F\)-alternating.
2. Condition (1.5) holds at every index.
3. The roots \(P_0,\ldots,P_{\ell-1}\) are pairwise distinct.

Consequently every admissible lifted cycle in the outgoing bank is clean
and coherently oriented as an abstract path-ledger switch. A three-cycle
gives a clean \(C_6\), a four-cycle gives a clean star \(C_8\), and no
folded \(C_6\) can arise from this matching orientation.

#### Proof

The equivalence of 1 and 2 is the definition of alternation, since the
first half of every edge pair is already in \(M^\uparrow\).

Every Chung--Feller row

\[
                         X_0(P),X_1(P),\ldots,X_r(P)                 \tag{1.7}
\]

is a Johnson geodesic from an \(r\)-set to its complement. Hence

\[
                         d_J(X_s(P),X_t(P))=|s-t|.     \tag{1.8}
\]

Two different states in the same \(K\)-fibre have Johnson distance one.
Thus, if \(P_i=P_j\), then \(|t_i-t_j|=1\); the two states are consecutive
on their old row. Let the earlier one be \(X_i=K+a_i\). Its successor is
necessarily the other state \(K+a_j\), and its intervening upper state is

\[
                         K+a_i+a_j.                   \tag{1.9}
\]

The outgoing arc from \(a_i\) is therefore \(a_i\to a_j\). Since (1.3)
uses the unique outgoing arc, \(j=i+1\) cyclically, and

\[
                         Y_iX_{i+1}\in M^\downarrow.  \tag{1.10}
\]

So condition 2 fails.

Conversely, if (1.5) fails, the two factor edges
\(X_iY_i\in M^\uparrow\) and \(Y_iX_{i+1}\in M^\downarrow\) are consecutive
on one old path. Hence \(P_i=P_{i+1}\). This proves 2 iff 3.

When the roots are distinct, all selected edges lie on distinct paths.
They are all traversed from \(X\) to \(Y\), so the clean-splice theorem
applies with one coherent sign. The last assertions follow. \(\square\)

### Example 1.2 (the smallest failure of the uncorrected implication)

At \(r=2\), the canonical rows are

\[
 12-124-14-134-34,
 \qquad
 13-123-23-234-24.                                    \tag{1.11}
\]

For the ballot-eligible core \(K=\{1\}\), the outgoing arcs are

\[
                         2\to4\to3\to2.               \tag{1.12}
\]

But the proposed new edge \(124-14\) is already in \(M^\downarrow\).
Thus (1.12) is a directed functional cycle but not an alternating cycle of
\(F\). This is exactly the obstruction detected by Proposition 1.1.

## 2. The rank-three clean star router

Use local coordinates \([6]\). Four canonical Chung--Feller rows have the
following relevant outgoing edges:

\[
\begin{array}{c|c|c|c}
\text{root word}&\text{root set}&\text{phase state}&\text{upper state}\\ \hline
110100&124&X_0=124&1246\\
111000&123&X_2=146&1456\\
110010&125&X_1=145&1345\\
101100&134&X_0=134&1234.
\end{array}                                             \tag{2.1}
\]

They form the literal incidence cycle

\[
 \boxed{
 124-1246-146-1456-145-1345-134-1234-124.}             \tag{2.2}
\]

Its common lower core is \(K_*=\{1,4\}\), and its petal cycle is

\[
                         2\to6\to5\to3\to2.           \tag{2.3}
\]

The four roots in (2.1) are distinct. Proposition 1.1 therefore proves
that (2.2) is a clean, coherently oriented, factor-alternating star
\(C_8\). Toggling it induces a four-cycle on the four root strands.

The deficient word of \(K_*\) is

\[
                         100100.                       \tag{2.4}
\]

It attains height one, so it is not nonpositive. By the ballot criterion
of Theorem 3.6, \(K_*\) is one of the eligible cores. Thus (2.2) is not an
external gadget imposed on the count: it is an abstractly
strand-admissible member of the ballot-forced bank.

## 3. Context suspension and the dense suffix bank

Fix \(r\ge3\) and \(0\le q\le r-3\). Let \(A\) and \(B\) be Dyck words
of semilengths \(q\) and \(r-q-3\), respectively. Consider the four roots

\[
 \begin{aligned}
 A110100B,\qquad A111000B,\qquad
 A110010B,\qquad A101100B.                            \tag{3.1}
 \end{aligned}
\]

The MSW concatenation law says that the complete block \(A\) is processed
before the displayed six-coordinate block, and that \(B\) is processed
after it. During the three central phases, the coordinates in \(A\) and
\(B\) form a common spectator: the \(A\)-part is the complement of the
up-step set of \(A\), while the \(B\)-part is still its root state.
Adjoining this spectator and shifting the local coordinates embeds (2.2)
literally in the rank-\(r\) factor.

### Theorem 3.1 (exact contextual router count)

For fixed \(q\), as \((A,B)\) ranges over

\[
                         D_{2q}^0\times D_{2(r-q-3)}^0,              \tag{3.2}
\]

the suspended cycles form

\[
                         \operatorname {Cat}_q
                         \operatorname {Cat}_{r-q-3}                \tag{3.3}
\]

pairwise vertex-disjoint clean star-\(C_8\) abstract path-ledger switches.
Their selected edge phases are

\[
                         q,\quad q+2,\quad q+1,\quad q.              \tag{3.4}
\]

Consequently:

1. every switch is factor-alternating and strand-admissible in the abstract
   middle-levels path ledger;
2. every selected and inserted cycle vertex occurs at or after phase
   \(q\), so the bank avoids every protected prefix of length at most
   \(q\);
3. any subfamily may be toggled simultaneously as a degree-exact
   root-to-complement-set path cover; and
4. the bank affects exactly
   \(4\operatorname {Cat}_q\operatorname {Cat}_{r-q-3}\) distinct root
   rows.

#### Proof

Concatenation gives the stated spectator extension and shifts the four
local phase labels \((0,2,1,0)\) by \(q\), proving (3.4). The four local
roots are distinct, so each suspended cycle is clean by Proposition 1.1.

For fixed \(q\), the decomposition into \(A\), the displayed six symbols,
and \(B\) is unique. Hence distinct pairs \((A,B)\) give disjoint sets of
four roots. The canonical factor is a vertex partition, so selected
vertices belonging to these disjoint old paths are distinct. Each new
half-edge stays inside the eight vertices of its own displayed cycle.
Thus the cycles are pairwise vertex-disjoint and may be toggled
independently.

No cycle vertex belongs to a state before phase \(q\), proving the prefix
claim. Four distinct old rows occur per context, proving the last count.
\(\square\)

### Corollary 3.2 (dense suffix bank)

Take \(q=r-3\), so \(B\) is empty. Then the bank has
\(\operatorname {Cat}_{r-3}\) routers, avoids every protected initial
prefix ending before phase \(r-3\), and affects the fraction

\[
 {4\operatorname {Cat}_{r-3}\over\operatorname {Cat}_r}
 ={r(r-1)(r+1)\over2(2r-1)(2r-3)(2r-5)}
 \longrightarrow {1\over16}.                         \tag{3.5}
\]

This is the requested \(\Omega(\operatorname {Cat}_r)\) affected-row
bank. No \(1/r\) loss occurs.

### Proposition 3.3 (ballot eligibility survives the context)

Let \(S_{A,B}\) be the common \((r-1)\)-core of the suspended router. Its
incidence word is

\[
                         \overline A\,100100B,         \tag{3.6}
\]

where \(\overline A\) is bitwise complement. This deficient path is not
nonpositive, and hence \(S_A\) is counted in \(Z_r\).

#### Proof

The complement of a Dyck word is nonpositive and ends at height zero. The
first symbol of the six-letter block in (3.6) is an up-step, so the total
path then reaches height one. It is therefore not nonpositive, regardless
of the later suffix \(B\). The exact ballot criterion from Theorem 3.6 says
precisely that such a core has no barred port extension. \(\square\)

Thus the contexts in Theorem 3.1 give distinct, explicitly identified
eligible cores among the \(Z_r\) counted in (0.1).

## 4. Endpoint action and the orbit-length ledger

Order the four selected edges as displayed in (2.2), and write their old
root strands as

\[
                         R_0,R_1,R_2,R_3.              \tag{4.1}
\]

Their cut phases are

\[
                         (t_0,t_1,t_2,t_3)=(q,q+2,q+1,q).           \tag{4.2}
\]

The new half-edge from the suffix side of cut \(i\) joins the prefix side
of cut \(i+1\). Hence the root \(R_{i+1}\) receives the old suffix of
\(R_i\). The endpoint action is the four-cycle

\[
                         (R_0\ R_1\ R_2\ R_3)^{-1}.    \tag{4.3}
\]

A root receiving the suffix from cut \(i\) at its own cut \(i+1\) has
new semilength

\[
                         r+t_{i+1}-t_i.                \tag{4.4}
\]

Substitution of (4.2) gives, in cyclic receiving order,

\[
                         r+2,\quad r-1,\quad r-1,\quad r.           \tag{4.5}
\]

Their sum is \(4r\). Therefore one toggle is orbit-length balanced for its
four-cycle twist. Four coherently transported copies pass both endpoint
monodromy and total-length closure:

\[
                         \tau^4=1,
 \qquad
                         \sum_{R\in\operatorname {Orb}(\tau)}q(R)=4r.
                                                                    \tag{4.6}
\]

This is the formal variable-length equation in the finite-order repetition
theorem. It does not make the switch a physical minimum-wreath slab. The
next section shows that even a common moving exterior cannot realize these
four rows geodesically.

## 5. Geodesicity obstructs physical realization

Let a candidate slab have local coordinate set \(J\), left and right
exteriors \(O_L,O_R\) of the same size, both disjoint from \(J\), and

\[
                         e=|O_L\setminus O_R|.         \tag{5.1}
\]

If it sends the local port \(P\) to the complementary port
\(J\setminus\tau(P)\), then

\[
\boxed{
 d_J\bigl(O_L\cup P,O_R\cup(J\setminus\tau(P))\bigr)
                         =e+|P\cap\tau(P)|.}           \tag{5.2}
\]

Indeed, if the ambient middle sets have size \(m\) and \(|P|=r\), their
intersection has size

\[
 (m-r-e)+(r-|P\cap\tau(P)|)=m-e-|P\cap\tau(P)|,
\]

which proves (5.2).

Every contiguous subpath of a minimum wreath is a Johnson geodesic.
Therefore an ordinary \(r\)-step slab requires

\[
                         e=r-|P\cap\tau(P)|
                          =|P\setminus\tau(P)|         \tag{5.3}
\]

for every strand. In particular \(e=0\) forces \(\tau(P)=P\) pointwise.

### Theorem 5.1 (the dense \(C_8\) bank is not a common-exterior packet)

For one contextual switch, order the local root ports as

\[
 \begin{aligned}
 R_0&=A110100B,&R_1&=A111000B,\\
 R_2&=A110010B,&R_3&=A101100B.                         \tag{5.4}
 \end{aligned}
\]

The endpoint twist is

\[
 R_0\mapsto R_3,\qquad R_1\mapsto R_0,\qquad
 R_2\mapsto R_1,\qquad R_3\mapsto R_2.               \tag{5.5}
\]

Its port displacements are

\[
 \bigl|R_i\setminus\tau(R_i)\bigr|=(1,1,1,2).        \tag{5.6}
\]

Consequently no ordinary \(r\)-step realization exists with one common
pair \((O_L,O_R)\). For the actual new semilengths

\[
 (q(R_0),q(R_1),q(R_2),q(R_3))=(r,r+2,r-1,r-1),      \tag{5.7}
\]

geodesicity would instead require

\[
 e_i=q(R_i)-|R_i\cap\tau(R_i)|=(1,3,0,1),             \tag{5.8}
\]

which again is not constant. Thus the literal toggled paths cannot occur
as four subpaths sharing one moving exterior either.

#### Proof

All four roots have the same \(r-3\) coordinates contributed by \(A,B\).
On the local six coordinates, the successive source--target pairs in
(5.5) are

\[
 124\to134,\qquad123\to124,\qquad
 125\to123,\qquad134\to125.                           \tag{5.9}
\]

The first three pairs differ in one element and the last differs in two,
proving (5.6). Equation (5.3) then rules out a common exterior for a strict
\(r\)-step slab.

The lengths in (5.7) are (4.5). The corresponding intersection sizes are
\(r-1,r-1,r-1,r-2\). A geodesic of the actual length \(q(R_i)\) would need
\(q(R_i)=e+|R_i\cap\tau(R_i)|\), which gives (5.8). \(\square\)

The only possible physical successor is a larger construction in which
the exterior/collar data depend on the transported strand, or in which
additional switches change the endpoint action to one of constant Johnson
displacement. Either route must prove the complete crossing \(X/Y\) ledger;
formal multiplication of the endpoint four-cycles is insufficient.

## 6. Exact audit verdict

The forced-bank statements now separate as follows.

| Router type | What the outgoing ballot bank proves |
|---|---|
| Clean \(C_6\) | No general positive count follows from \(Z_r\) alone. Any valid directed three-cycle is automatically clean only in the abstract path ledger. |
| Folded \(C_6\) | Exactly zero: a repeated strand forces one proposed new edge to lie in \(M^\downarrow\), so the cycle is not alternating. |
| Clean star \(C_8\) | At least \(\operatorname {Cat}_{r-3}\) pairwise vertex-disjoint abstract suffix switches, affecting \(4\operatorname {Cat}_{r-3}=(1/16+o(1))\operatorname {Cat}_r\) rows; Theorem 5.1 forbids their realization with one common exterior. |
| Longer directed cycles | Admissible exactly when their phase-labelled roots are distinct in the abstract ledger; no physical density claim follows. |

Accordingly, the unqualified sentence "every eligible core contains an
alternating incidence cycle" must be replaced by the full-factor criterion
of Proposition 1.1. After that correction, the ballot route is
scalar-sufficient only at the abstract incidence level: the suffix \(C_8\)
family supplies a positive Catalan fraction and avoids the protected
prefix.

For coefficient one, cycle density is no longer the first missing gate.
The pure suffix bank cannot supply a common-exterior packet. A bounded
literal repair does exist--the five-strand pentagon completion proved in
`MATH_THEOREM_SUFFIX_C8_LITERAL_PENTAGON_COMPLETION_AND_PURE_BANK_OBSTRUCTION_20260726.md`--but it absorbs one arm of the clean \(C_8\), so its carrier
must be recalculated from scratch. Any repair intended to retain the clean
\(C_8\) carrier needs either a new fixed-exterior interaction or a genuinely
exterior-moving packet with the full crossing-collar ledger.
