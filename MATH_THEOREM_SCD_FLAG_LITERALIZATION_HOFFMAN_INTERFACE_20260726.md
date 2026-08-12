# SCD flag literalization: an exact Hoffman-compatible mixed-frame interface

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Verdict

Put

\[
 \mathcal M=\binom{[2m]}m,
 \qquad W=|\mathcal M|,
 \qquad
 \mathcal L_q^\pm=\binom{[2m]}{m\pm q}.
\tag{0.1}
\]

The polynomial mixed-frame theorem gives excellent unfrozen literal Hall
expansion at every depth, but choosing its depthwise matchings independently
does not force nested prefixes.  There is nevertheless an exact positive
interface theorem if the frame catalogue is enlarged from polynomial size to
subexponential size.

### Theorem 0.1 (exact two-sided flag literalization)

Let \(1\le H\le m/4\).  There are

\[
 J\le C m\,4^H\exp\!\left(C{H^2\over m}\right)
\tag{0.2}
\]

coordinate-pair frames, one frame assignment

\[
 \phi:\mathcal M\longrightarrow[J],
\tag{0.3}
\]

and, for every \(q\le H\), injective target-to-owner maps

\[
 \mu_q^-:\mathcal L_q^-\longrightarrow\mathcal M,
 \qquad
 \mu_q^+:\mathcal L_q^+\longrightarrow\mathcal M,
\tag{0.4}
\]

with the following properties.

1.  Every target is assigned literally:

    \[
      T\subset\mu_q^-(T),
      \qquad
      \mu_q^+(T)\subset T.
    \tag{0.5}
    \]

2.  For each owner \(X\), all lower targets assigned to \(X\) are prefixes
    of one deletion order in the single frame \(P_{\phi(X)}\), and all upper
    targets assigned to \(X\) are prefixes of one addition order in that
    same frame.  The lower and upper marked directions can in fact be made
    disjoint.

3.  Give each physical target the induced frame

    \[
      \psi_q^\pm(T)=\phi(\mu_q^\pm(T)).
    \tag{0.6}
    \]

    In the fixed-target-frame layered pair-flip networks, with unit owner
    roots and lower throughput one at every assigned target, there is an
    explicit integral feasible flow.  Consequently every Hoffman cut holds
    simultaneously at all depths and on both sides.

4.  If

    \[
      H\le C_0\sqrt{m\log m},
    \tag{0.7}
    \]

    the selected frame of every owner may additionally be required to have
    balanced pair type

    \[
      |f_{P_{\phi(X)}}(X)-\mu_0|
      \le A_0\sqrt{m\log m},
      \qquad
      \mu_0={m(m-1)\over2(2m-1)},
    \tag{0.8}
    \]

    where \(A_0=A_0(C_0)\) is a sufficiently large constant.

Thus, in the calibrated range (0.7),

\[
 J=\exp(O(\sqrt{m\log m}))=W^{o(1)},
 \qquad HJ=o(W).
\tag{0.9}
\]

There are **no exceptional targets** in this interface theorem.  In
particular, if changing or opening one frame costs \(O(H)\), the total
frame-interface toll is \(o(W)\).

The qualification is exact: this proves the interface after a
\(W^{o(1)}\)-size frame augmentation.  It does not prove that the original
polynomial catalogue contains a Hoffman-compatible choice.  For a fixed
predeclared two-sided flag, a random frame succeeds with probability only
\(4^{-H}\exp(-O(H^2/m))\), so a polynomial random catalogue literalizes only
an \(o(1)\) fraction of any fixed SCD flag system when \(H\to\infty\).  A
polynomial-catalogue proof must therefore choose the flags adaptively; it
cannot use the fixed-flag union bound below.

## 1. One simultaneous target-to-owner system from an SCD

Use a symmetric chain decomposition of the Boolean lattice
\(2^{[2m]}\).  Every symmetric chain has the form

\[
 S_d\subset S_{d+1}\subset\cdots\subset S_{2m-d},
 \qquad |S_i|=i,
\tag{1.1}
\]

and therefore contains exactly one middle set \(X=S_m\).  Conversely every
middle set is the middle member of exactly one chain.  Write \(C_X\) for
that chain and \(d_X=m-d\) for its lower and upper radius.

Going downward and upward from \(X\), write

\[
 S_{m-q}=X\setminus\{a_1(X),\ldots,a_q(X)\},
\tag{1.2}
\]

\[
 S_{m+q}=X\cup\{b_1(X),\ldots,b_q(X)\}
\tag{1.3}
\]

for \(q\le d_X\).  Extend \(a_1(X),\ldots,a_{d_X}(X)\) arbitrarily to an
ordered list of \(H\) distinct elements of \(X\), and extend the \(b\)-list
arbitrarily to \(H\) distinct elements of \(X^c\).  This is possible since
\(H\le m\).  Put

\[
 A_X=\{a_1(X),\ldots,a_H(X)\}\subset X,
 \qquad
 B_X=\{b_1(X),\ldots,b_H(X)\}\subset X^c.
\tag{1.4}
\]

For a lower target \(T\in\mathcal L_q^-\), let \(C_X\) be its unique SCD
chain and define \(\mu_q^-(T)=X\).  Define \(\mu_q^+\) in the same way on
the upper side.

### Lemma 1.1 (exact Boolean ownership and coherence)

For every \(q\le H\), both maps in (0.4) are injective.  Every target is
assigned once, and if targets at several depths are assigned to the same
owner, then they are the nested prefixes (1.2), respectively (1.3).

#### Proof

Every target belongs to exactly one SCD chain.  A chain contains at most
one set of a given rank, so two distinct rank-\((m-q)\) targets cannot be
assigned to the same middle owner; this proves injectivity below the
middle.  The upper proof is identical.  If a chain reaches rank \(m-q\),
then its lower and upper members are exactly (1.2) and (1.3).  The arbitrary
extensions in (1.4) occur only beyond the end of that chain and do not
alter any assigned target. \(\square\)

The standard existence theorem for symmetric chain decompositions is the
only Boolean-lattice input here.  For completeness, its induction sends a
chain

\[
 A_k\subset A_{k+1}\subset\cdots\subset A_{n-k}
\]

in \(2^{[n]}\) to the two chains

\[
 A_k\subset\cdots\subset A_{n-k}
       \subset A_{n-k}\cup\{n+1\},
\]

\[
 A_k\cup\{n+1\}\subset\cdots\subset
       A_{n-k-1}\cup\{n+1\},
\]

with the second chain omitted when it is empty.  These chains partition
the two copies of the original chain, and each is saturated and symmetric.
Starting from \(2^{[1]}\) proves existence in every dimension.

## 2. Probability that one frame literalizes both flags

Fix an owner \(X\), and abbreviate \(A=A_X\), \(B=B_X\).  Let \(P\) be a
uniform perfect matching of \([2m]\).  Consider the following stronger
event \(E_X\):

* every vertex of \(A\) is paired into \(X^c\setminus B\);
* every vertex of \(B\) is paired into \(X\setminus A\).

On \(E_X\), the \(2H\) marked vertices use \(2H\) distinct cross-edges.
Consequently all \(a_i(X)\) and \(b_i(X)\) lie in split pairs of \(X\),
the lower directions are distinct, the upper directions are distinct, and
the two direction families are disjoint.

There are

\[
 ((m-H)_{\underline H})^2
\tag{2.1}
\]

ways to choose the two injective partner maps in \(E_X\).  Each choice
specifies \(2H\) disjoint matching edges.  A uniform perfect matching
contains a fixed collection of \(2H\) disjoint edges with probability

\[
 {1\over(2m-1)(2m-3)\cdots(2m-4H+1)}.
\tag{2.2}
\]

The partner maps are recovered uniquely from the resulting matching, so
there is no overcount.  Therefore

\[
 p_H:=\Pr(E_X)
 ={((m-H)_{\underline H})^2
   \over
   \prod_{i=0}^{2H-1}(2m-2i-1)}.
\tag{2.3}
\]

Uniformly for \(H\le m/4\),

\[
 \boxed{
 p_H\ge4^{-H}\exp\!\left(-C{H^2\over m}\right).}
\tag{2.4}
\]

Indeed,

\[
 (m-H)_{\underline H}
 =m^H\exp\!\left(-O(H^2/m)\right),
\tag{2.5}
\]

while the denominator in (2.3) is at most \((2m)^{2H}\).  A rough bound
valid throughout \(H\le m/4\) is \(p_H\ge16^{-H}\).

### Lemma 2.1 (balanced literalization)

Under (0.7), and for \(A_0(C_0)\) sufficiently large,

\[
 \Pr\bigl(E_X\ \hbox{and}\ 
 |f_P(X)-\mu_0|\le A_0\sqrt{m\log m}\bigr)
 \ge {p_H\over2}
\tag{2.6}
\]

for all sufficiently large \(m\).

#### Proof

Condition on one of the partner-map choices in \(E_X\).  After its
\(2H\) forced cross-edges are removed, there remain \(m-2H\) vertices of
\(X\) and \(m-2H\) vertices of \(X^c\), and the remaining matching is
uniform.  The number of its edges internal to the first shore has mean

\[
 {(m-2H)(m-2H-1)\over2(2m-4H-1)}
 ={m-2H\over4}+O(1).
\tag{2.7}
\]

Exposure of the remaining matching gives a bounded-difference martingale,
so for an absolute \(c>0\),

\[
 \Pr(|f_P(X)-\mathbb Ef_P(X)|>t\mid E_X)
 \le2\exp(-ct^2/m).
\tag{2.8}
\]

The conditional mean differs from \(\mu_0\) by at most \(H/2+O(1)\).
Under (0.7), choosing \(A_0>C_0/2\) with a fixed additional margin makes
the complement of (0.8) have conditional probability \(o(1)\), uniformly
in \(X\).  It is at most \(1/2\) for large \(m\), which proves (2.6).
\(\square\)

## 3. A common catalogue by one union bound

Choose \(J\) independent uniform pair frames.  Without (0.7), use the
event \(E_X\) itself.  Under (0.7), use its balanced strengthening from
Lemma 2.1.  In either case the success probability is at least \(p_H/2\),
so for one fixed owner the probability that no frame succeeds is at most

\[
 \exp(-Jp_H/2).
\tag{3.1}
\]

Since \(W\le4^m\), choosing

\[
 J=\left\lceil{4m\over p_H}\right\rceil
\tag{3.2}
\]

gives

\[
 \Pr(\hbox{some owner has no compatible frame})
 \le4^m e^{-2m}<1.
\tag{3.3}
\]

Thus a deterministic catalogue exists.  Equations (2.4) and (3.2) give
(0.2).  Assign each owner one successful frame and call it \(\phi(X)\).

For this frame, deleting \(a_1(X),\ldots,a_H(X)\) in order is a legal
pair-flip path, because each \(a_i(X)\) is the selected endpoint of a
different split pair.  Adding \(b_1(X),\ldots,b_H(X)\) is a legal upper
path for the same reason.  This proves the literal part of Theorem 0.1.

For (0.9), (2.4) gives

\[
 \log J\le H\log4+O(H^2/m+\log m)=o(m),
\tag{3.4}
\]

whereas \(\log W=(2\log2+o(1))m\).  Hence \(J=W^{o(1)}\), and multiplication
by \(H=m^{O(1)}\) still gives \(HJ=o(W)\).

## 4. Exact Hoffman verification

Assign every lower target \(T\) to the frame

\[
 \psi_q^-(T)=\phi(\mu_q^-(T)),
\tag{4.1}
\]

and do the same above the middle.  These are genuine partitions of the
physical targets: every target has one owner under Lemma 1.1 and every
owner has one frame under Section 3.

In the lower fixed-frame layered network, send one unit from every owner
\(X\) along

\[
 X,
 X\setminus\{a_1(X)\},
 \ldots,
 X\setminus\{a_1(X),\ldots,a_H(X)\}.
\tag{4.2}
\]

If \(T\in\mathcal L_q^-\) is assigned to \(X\), then \(q\le d_X\) and
the level-\(q\) state in (4.2) is exactly \(T\).  Thus the throughput of
the node \((\psi_q^-(T),q,T)\) is at least one.  Root supplies are exactly
one and every used transition is a legal pair flip.  Therefore (4.2) is
an integral feasible flow for the complete set of assigned lower bounds.

The upper paths defined by the \(b_i(X)\)'s give the upper integral flow.
Both use the same owner-frame assignment.  By summing conservation over
an arbitrary vertex set, either explicit flow gives

\[
 \ell(\delta^-(S))\le u(\delta^+(S))
\tag{4.3}
\]

for every Hoffman cut \(S\).  This proves item 3 of Theorem 0.1 directly;
total unimodularity is needed only for the converse statement that the cut
inequalities would also suffice.

The statement concerns the natural coverage network: unit owner roots,
legal transition arcs, and mandatory throughput one at the unique assigned
frame-copy of each target.  Extra artificial upper quotas are valid only
if they dominate the explicit loads in (4.2); arbitrary independently
prescribed frame/type quotas are not asserted.

## 5. Relation to the unfrozen mixed-frame Hall theorem

At each fixed depth, Lemma 1.1 already gives an inclusion matching
saturating every target.  Sections 2--3 decorate all of these matchings,
simultaneously, by one literal frame per owner.  Hence the result may be
viewed as a coherent strengthening of the unfrozen one-depth Hall
conclusion after subexponential frame augmentation:

\[
 \begin{array}{c}
 \text{one target-to-owner matching at every depth}\\
 +\text{one common owner frame}\\
 +\text{one common lower/upper flag per owner}.
 \end{array}
\tag{5.1}
\]

No target-frame rounding matrix is used, so the determinant-two linking
minor and possible odd-set corrections are bypassed rather than assumed
away.

There is no direct matroid theorem hidden in one frame block.  Take one
owner with distinct legal split-pair deletions \(a,b,c\).  One path visits

\[
 A_1=X\setminus\{a\},\qquad
 A_2=X\setminus\{a,b\},
\]

while another visits \(B_1=X\setminus\{c\}\).  The visitable target
families contain \(\{A_1,A_2\}\) and \(\{B_1\}\), but neither
\(\{B_1,A_1\}\) nor \(\{B_1,A_2\}\) is visitable by one path.  Thus the
hereditary path-incidence family fails the matroid augmentation axiom.
Accordingly the fixed-frame TU flow should not be projected and treated
as a matroid rank oracle; its integrality lives in the extended arc-flow
space.  The construction above keeps that extended witness explicit.

If \(\mathscr P_0\) is the polynomial catalogue from the unfrozen
mixed-frame Hall theorem, take the union of \(\mathscr P_0\) with the
catalogue constructed in Section 3.  Adding frames deletes no literal edge
and invalidates no previously proved Hall inequality.  The total catalogue
still has size \(W^{o(1)}\), while the distinguished SCD matchings use the
new frames to satisfy the stronger multidepth Hoffman system.  Thus the
theorem is a genuine augmentation of the unfrozen construction, not a
replacement of its one-depth conclusions.

There is also a sharp warning about catalogue size.  Fix in advance the
SCD and all extensions (1.4).  Let \(\widetilde E_X\) be the full
compatibility event: every vertex of \(A_X\cup B_X\) is on a cross-edge
of the cut \((X,X^c)\).  Unlike \(E_X\), this permits a marked lower
vertex to be paired directly with a marked upper vertex.

If exactly \(k\) such \(A_X\)--\(B_X\) edges occur, choose their endpoints
and bijection, and then pair the remaining marked vertices outside the
opposite marked set.  The choices are disjoint and recoverable from the
matching, so the exact probability is

\[
 \Pr(\widetilde E_X)
 =
 \sum_{k=0}^H
 \binom Hk^2 k!\,
 {((m-H)_{\underline{H-k}})^2
  \over
  \prod_{i=0}^{2H-k-1}(2m-2i-1)}.
\tag{5.2}
\]

For \(H=o(m)\), comparison of the \(k\)-th summand with
\((2m)^{-(2H-k)}m^{2H-2k}\), absorbing the denominator distortion into
\(\exp(O(H^2/m))\), gives

\[
 \begin{aligned}
 \Pr(\widetilde E_X)
 &\le
 4^{-H}\exp(O(H^2/m))
 \sum_{k=0}^H {1\over k!}
       \left({2H^2\over m}\right)^k\\
 &\le4^{-H}\exp(O(H^2/m)).
 \end{aligned}
\tag{5.3}
\]

For a polynomial number \(J=m^{O(1)}\) of random frames, the expected
fraction of owners for which at least one frame realizes this fixed
two-sided flag is therefore at most

\[
 J\Pr(\widetilde E_X)
 \le m^{O(1)}4^{-H}\exp(O(H^2/m))=o(1)
\tag{5.4}
\]

whenever \(H/\log m\to\infty\) and \(H=o(m)\).  Markov's inequality then
shows that a fixed SCD flag system is almost entirely unavailable in the
polynomial random catalogue.  This is a method obstruction, not an
integrality-gap obstruction: an adaptive choice among the many possible
nested flags might still work with polynomially many frames.

The same argument rules out every small predeclared menu, not just one
SCD.

### Proposition 5.1 (positive-density obstruction to bounded flag menus)

Before sampling the frames, give every owner a menu of at most \(R\)
two-sided length-\(H\) flags.  The menus may vary arbitrarily with the
owner.  For \(J\) independent uniform frames, put

\[
 \eta_{H,R,J}
 =RJ\,4^{-H}\exp(O(H^2/m)).
\tag{5.5}
\]

If \(\eta_{H,R,J}=o(1)\), then with probability \(1-o(1)\) only
\(o(W)\) owners have even one menu flag compatible with even one catalogue
frame.

#### Proof

For a fixed owner, flag, and frame, (5.3) bounds the compatibility
probability.  A union bound over its at most \(RJ\) flag--frame pairs gives
probability at most \(\eta_{H,R,J}\) that the owner is serviceable.
Therefore the expected number of serviceable owners is at most
\(\eta_{H,R,J}W=o(W)\).  Markov's inequality proves the claim.
\(\square\)

In particular, polynomial \(R\) and polynomial \(J\) fail whenever
\(H/\log m\to\infty\) and \(H=o(m)\).  This is an asymptotic
positive-density obstruction, stronger than a finite determinant-two
minor: the standard random polynomial catalogue can satisfy all of the
unfrozen mixed-frame Hall estimates while simultaneously leaving
\((1-o(1))W\) owners outside every predeclared polynomial flag menu.
It still does not rule out a frame-dependent adaptive flag construction
with exponentially many implicit choices.

## 6. Exact surviving gate

The target/frame/nested-prefix interface now has the following dichotomy.

* With \(J=\exp(O(H+H^2/m))=W^{o(1)}\) frames, exact Boolean ownership,
  two-sided nested coherence, and every Hoffman cut are simultaneously
  satisfied with zero exceptions.
* With the original polynomial catalogue, the known unfrozen Hall theorem
  and the known \(o(W)\) sum of frozen one-depth Hall deficiencies do not
  yet imply the multidepth Hoffman system.  A proof there must adapt the
  flag system to the available frames using more than a polynomial
  predeclared menu, or establish a new dependent matching theorem for the
  projected nested-flow polytope.

Whole-cycle bundling remains separate.  The assignment \(\phi\) constructed
here is ownerwise and need not make its frame classes unions of complete
isometric cycles.  Therefore the present theorem closes the literal
target/frame/Hoffman interface at subexponential frame complexity, but it
does not by itself close the final cycle-factor gate.

### Subsequent whole-cycle audit

MATH_THEOREM_PHASE_FLAG_CYCLE_HYPERGRAPH_AND_ADAPTIVITY_OBSTRUCTION_20260726.md
computes the exact hypergraph of \(C_{2h}\) phase flags.  A flag has degree
\((h-H)!\), but its antipodal twin has the same link, so the uncontracted
maximum codegree equals the degree.  After antipodal contraction the
nontrivial relative codegree is at most \(2/(h-H)\); nevertheless an
independent choice of one flag per owner leaves at most an
\(\exp(-h+O(\log h))\) expected coverable fraction.  Thus the present
ownerwise literalization cannot be converted by a generic post hoc nibble.
Cycles and their correlated flags must be chosen first, after which target
ownership/Hoffman feasibility must be recovered from their actual phase
incidences.
