# Safe de Bruijn ports versus the full common-template Markov basis

## A splice-noncongruence and persistent exponential minors

Date: 2026-07-26

Scope: constant-one Gaussian-annulus program; pure mathematics only.
No computation, search, solver, or external theorem is used.

## 0. Verdict

The audited higher placeholder cubes and the physical directed-cycle
reversals do not remove the safe de Bruijn diagonal-pairing obstruction
by quotienting.

There are two exact reasons.

1.  They are kernel moves for the all-depth target-load map, but they
    are not kernel moves for the ordered splice-port map.  Already in
    the fixed-core tournament sector, one common marked port window
    containing placeholder \(P\) and not placeholder \(Q\) recovers
    the orientation of every pair top.  Hence it recovers the whole
    tournament.  The triangle Markov basis connects the score fibre
    only after this marked-port information has been forgotten.

2.  In every literal occurrence/port formulation, adjoining arbitrary
    directed-cycle moves, arbitrary audited \(2^k\)-corner placeholder
    cubes, and arbitrary further load or port rows leaves the old
    determinant minors in place.  At full protected depth their
    magnitude is

    \[
       2^{\lfloor (m+H+1)/(3H+2)\rfloor}
       =2^{\Theta(m/H)}.                                      \tag{0.1}
    \]

Thus there is a precise dichotomy.

* Quotient by the full common-template cycle Markov relation: the
  all-depth load fibre becomes connected, but literal splicing is not
  well defined on the quotient.
* Retain enough information to reconstruct literal incoming and
  outgoing ports: the full Markov relation is no longer available, and
  the exponential safe-port minors survive.

This is an obstruction to a TU/network-flow or ``quotient first, splice
later'' proof.  It is not a proof that carefully chosen physical cycle
moves cannot help a construction which tracks and rechecks every
changed collar explicitly.

## 1. Safe ports and the two maps

Put

\[
                         N=2m,\qquad M=m+H,
\tag{1.1}
\]

and fix a protected depth \(1\le \delta\le H\).  The safe de Bruijn
memory and port length are

\[
                         \ell=H+\delta,
             \qquad     L=\ell-1.                              \tag{1.2}
\]

Throughout the Gaussian regime \(H<m\), and therefore

\[
                         1\le L<M.                              \tag{1.3}
\]

For a top \(U\) of size \(M\), a safe state is an injective ordered word

\[
                         v=(z_1,\ldots,z_L)\in U^L.             \tag{1.4}
\]

A safe arc is an injective \(\ell\)-word

\[
 e=(z_0,z_1,\ldots,z_L),qquad
 \partial^-e=(z_0,\ldots,z_{L-1}),\quad
 \partial^+e=(z_1,\ldots,z_L).                                \tag{1.5}
\]

The root, top, ordered tail, ordered head, and all signed target labels
belong to the **literal splice signature** of \(e\).  Let

\[
                         \mathsf P(e)                           \tag{1.6}
\]

denote this signature.  Formally, linearize it into the free abelian
group on marked-location/signature pairs: an occurrence contributes one
basis vector at each of its marked entry and exit locations.  For a
marked frame table, \(\mathsf P\) is therefore the integral incidence
vector of the marked signatures, with the top/root coordinate retained.
Thus signatures from two different tops are never cancelled against
one another, and \(\ker_{\mathbb Z}\mathsf P\) has its literal linear
meaning.

Let \(\mathsf A\) be the common-template all-depth load map: its rows
are the top rows and every scheduled physical target row.  The
distinction to be maintained is

\[
 \ker_{\mathbb Z}\mathsf A
 \quad\hbox{versus}\quad
 \ker_{\mathbb Z}\mathsf A\cap\ker_{\mathbb Z}\mathsf P.      \tag{1.7}
\]

The first is the unmarked toric move lattice.  Only the second consists
of moves invisible to literal marked splicing.

## 2. The exact splice-congruence criterion

For a safe state \(v\), let its right continuation language be

\[
 \mathcal N^+(v)
   =\{(v,y):y\in U\setminus\operatorname{supp}(v)\}.           \tag{2.1}
\]

Here \((v,y)\) denotes the injective \(\ell\)-word having tail \(v\).
Define the left language analogously.

### Lemma 2.1 (ports are separated by their continuation languages)

For safe states \(v,v'\) on the same top,

\[
             \mathcal N^+(v)=\mathcal N^+(v')
             \quad\Longleftrightarrow\quad v=v'.              \tag{2.2}
\]

The analogous statement holds on the left.

#### Proof

The reverse implication is immediate.  If \(v\ne v'\), every arc in
\(\mathcal N^+(v)\) has ordered tail exactly \(v\), so it is not an arc
in \(\mathcal N^+(v')\).  Moreover \(\mathcal N^+(v)\ne\varnothing\)
because \(L<M\).  Thus the two languages differ. \(\square\)

Let \(\sim\) be an equivalence relation on marked literal packets.  Call
it a **right splice congruence** if, whenever \(F\sim F'\), every fixed
literal continuation can be attached to \(F\) exactly when it can be
attached to \(F'\).  Define left splice congruence similarly.

### Corollary 2.2 (necessary and sufficient marked-port condition)

An equivalence relation is a left-and-right safe-de-Bruijn splice
congruence precisely when every pair of equivalent marked packets has
the same ordered entry and exit ports, including its root/top labels.

#### Proof

Equality of the ports plainly makes exact-overlap splicing invariant.
Necessity follows from Lemma 2.1 at every marked entry and exit.  The
root/top label is necessary because a safe overlap belongs to one
literal top, and same-owner switching between different collar tops is
not bridge-one. \(\square\)

Equivalently, if \(q\) is a quotient map, then the literal splice map
descends to the quotient only if

\[
                         \mathsf P=\overline{\mathsf P}\circ q \tag{2.3}
\]

for some quotient map \(\overline{\mathsf P}\).  In a quotient by a
move lattice \(\mathcal L\), condition (2.3) requires

\[
                         \mathcal L\subseteq\ker\mathsf P.     \tag{2.4}
\]

## 3. A single marked port recovers the fixed-core tournament

Fix an \((M-2)\)-set \(C\), two placeholder positions \(P,Q\) in a
cyclic positional word on \(C\cup\{P,Q\}\), and an outside label set
\(Z\).  Each pair top

\[
                         U_{uv}=C\cup\{u,v\}                   \tag{3.1}
\]

has two frames.  Write \(u\to v\) when \(u\) occupies \(P\) and \(v\)
occupies \(Q\).  A one-frame-at-each-pair-top table is a tournament
\(T\) on \(Z\).

Because \(1\le L<M\), there is a cyclic interval \(I\) of length \(L\)
which contains \(P\) and does not contain \(Q\): after deleting \(P\),
choose \(M-L\) consecutive remaining positions containing \(Q\), and
take their cyclic complement.  Mark at every pair top
the ordered port occupying these positions.  Let \(\mathsf P_I(T)\) be
the resulting top-indexed port profile.

### Theorem 3.1 (marked-port injectivity)

The map

\[
                    T\longmapsto \mathsf P_I(T)                \tag{3.2}
\]

is injective.  Consequently no nontrivial directed-cycle reversal lies
in \(\ker\mathsf P_I\).

#### Proof

At top \(U_{uv}\), the marked ordered word contains the label occupying
position \(P\), but not the label occupying position \(Q\).  It
therefore contains \(u\) in that distinguished position exactly when
\(u\to v\), and contains \(v\) there exactly when \(v\to u\).  Since
the top \(\{u,v\}\) is part of the profile, this recovers the
orientation of every edge.  Hence it recovers \(T\).

A nontrivial directed-cycle reversal changes at least one tournament
edge, so injectivity says that it changes \(\mathsf P_I\). \(\square\)

By contrast, the complete phase-refined all-depth load vector depends
only on the score sequence

\[
                         (d_T(u))_{u\in Z}.                     \tag{3.3}
\]

Triangle reversals connect every two tournaments with the same score
sequence.  Thus the unmarked Markov quotient collapses each score fibre,
whereas the marked-port profile separates every point of that fibre.
In this sector one has the exact identities

\[
 \begin{aligned}
  \mathcal L_{\rm cyc}
     &=\{T'-T:d_{T'}=d_T\},\\
  \mathcal L_{\rm cyc}\cap\ker\mathsf P_I
     &=\{0\}.
 \end{aligned}                                                  \tag{3.4}
\]

The second line is meant on differences of tournament tables.  It says
that after this literal port is retained, none of the nontrivial
fixed-score Markov freedom can be quotiented out.

## 4. Explicit failure of the triangle quotient to respect splicing

The preceding injectivity can be witnessed by one continuation.
Choose distinct \(a,b,c\in Z\) and a tournament containing

\[
                         a\to b\to c\to a.                     \tag{4.1}
\]

Let \(T'\) be obtained by reversing this directed triangle.  Every
vertex keeps its score, so \(T,T'\) have exactly the same top and
all-depth target loads.  They are the two sides of one physical
triangle move.

At top \(U_{ab}\), let \(v\) and \(v'\) be the marked exit ports in
\(T\) and \(T'\).  The label at position \(P\) is respectively \(a\)
and \(b\), so

\[
                         v\ne v'.                              \tag{4.2}
\]

Choose

\[
                         y\in U_{ab}\setminus\operatorname{supp}(v),
\tag{4.3}
\]

which is possible by \(L<M\), and take the safe continuation arc
\(g=(v,y)\).  It attaches literally to the marked packet of \(T\), but
not to the corresponding packet of \(T'\), because its tail is not
\(v'\).

### Theorem 4.1 (cycle Markov equivalence is not a splice congruence)

The equivalence relation generated by physical triangle reversals, and
hence the equivalence relation generated by all physical directed-cycle
reversals, is neither a right nor a left safe-de-Bruijn splice
congruence.

#### Proof

The right-hand assertion follows from (4.1)--(4.3).  Reverse the marked
cut to obtain the left-hand witness.  Since triangle reversals are among
the directed-cycle reversals, the same counterexample applies to the
larger relation. \(\square\)

Notice that both endpoints of the move are fully physical frame tables.
The failure is not the earlier clone-flow problem.  It occurs because
two literal physical tables with identical all-depth loads have
different legal continuation languages.

## 5. Higher \(2^k\)-corner cubes fail the same test

Consider an audited placeholder cube of dimension \(k\ge2\), with tops

\[
 U_\epsilon=C\cup\{a_{j,\epsilon_j}:1\le j\le k\},
 \qquad \epsilon\in\{0,1\}^k,                                 \tag{5.1}
\]

and two placeholder permutations \(\sigma\ne\tau\).  Its alternating
exchange is exact at every phase and interval length:

\[
 \sum_{\epsilon}(-1)^{|\epsilon|}
 \bigl(v_\epsilon^\sigma(s,r)-v_\epsilon^\tau(s,r)\bigr)=0.
                                                                    \tag{5.2}
\]

It also preserves the common retained phase set and therefore the
number of phase runs/components at every touched top.

### Theorem 5.1 (higher cubes are not port-kernel moves)

Every nontrivial higher placeholder cube has a marked safe port at
which its two sides have different literal splice signatures.  Hence
the equivalence relation generated by all such cubes is not a safe
splice congruence.

#### Proof

Since \(\sigma\ne\tau\), some placeholder position receives different
placeholder indices on the two sides.  Choose a length-\(L\) cyclic
port interval containing that position.  At every cube corner, the
labels attached to distinct placeholder indices are distinct, so the
ordered word in this port changes between the \(\sigma\)-frame and the
\(\tau\)-frame.

In the alternating compound exchange, choose any corner on which the
direction is \(\sigma\to\tau\) (the reverse direction gives the same
argument).  Because top identity is retained in \(\mathsf P\), a
change at this corner cannot cancel against a change at another corner.
Lemma 2.1 supplies a safe continuation legal on exactly one side.
Therefore the cube direction is not in \(\ker\mathsf P\), and its orbit
relation is not a splice congruence. \(\square\)

Equation (5.2) is therefore a load identity, not a port identity.  The
same conclusion holds for arbitrary common nested tags: common tags
make the target cancellation exact but do not identify the changed
ordered ports.

## 6. The exponential minors survive every literal augmentation

Suppose now that \(2\le\delta\le H\).  Let \(B_\delta\) be the
block-diagonal root-state incidence matrix of
the safe de Bruijn graphs of memory \(H+\delta\), and let \(C_0\) be
the middle-target incidence matrix.  The safe-cycle construction gives,
for

\[
 1\le r\le
 \left\lfloor\frac{M+1}{H+2\delta+2}\right\rfloor,             \tag{6.1}
\]

a square submatrix of

\[
                         \begin{pmatrix}B_\delta\\ C_0\end{pmatrix}
\tag{6.2}
\]

with determinant \(\pm2^r\).  The \(r\) blocks use private roots,
private safe states, and private twice-occurring targets.

### Theorem 6.1 (full common-template augmentation does not remove the minors)

Form any literal augmented system which retains the safe occurrence
columns and the rows in (6.2), and then adjoins any collection of

1. physical triangle or longer directed-cycle exchange columns;
2. audited higher \(2^k\)-corner cube exchange columns;
3. signed-depth target and common-tag rows;
4. ordered port, collar, seam, or component rows; and
5. auxiliary columns recording any compounds of the preceding moves.

The augmented matrix still contains a minor of determinant
\(\pm2^r\) for every \(r\) allowed by (6.1).

#### Proof

Select exactly the old rows and columns used in (6.2), and omit every
adjoined row and column.  The selected square submatrix is unchanged.
Its determinant is \(\pm2^r\). \(\square\)

At full protected depth \(\delta=H\), take

\[
 r=\left\lfloor\frac{m+H+1}{3H+2}\right\rfloor.               \tag{6.3}
\]

If \(H=o(m)\), then

\[
 r=\left(\frac13+o(1)\right)\frac mH.                         \tag{6.4}
\]

In particular, for a fixed Gaussian cutoff \(H=A\sqrt m\),

\[
 |\det|=2^{(1/(3A)+o(1))\sqrt m}.                              \tag{6.5}
\]

There is a slightly stronger column-quotient statement.  The chosen
safe-cycle arcs have pairwise distinct ordered tail/head signatures.
Consequently any quotient permitted to merge only columns with
identical literal splice signatures leaves those chosen columns in
distinct classes and leaves the same determinant block.  Eliminating
the block requires identifying configurations whose literal signatures
differ; Theorems 4.1 and 5.1 say precisely that such an identification
is not a physical splice quotient.

## 7. Exact quotient dichotomy

Let \(\mathcal L_{\rm full}\) be the integer lattice generated by the
full fixed-core directed-cycle Markov basis together with every audited
higher placeholder cube; let \(\sim_{\rm full}\) be the corresponding
equivalence relation generated by applicable physical moves.  Then

\[
                  \mathcal L_{\rm full}\subseteq\ker\mathsf A,
 \qquad
                  \mathcal L_{\rm full}\not\subseteq\ker\mathsf P.
                                                                    \tag{7.1}
\]

The first inclusion is the all-depth cancellation theorem.  The second
is witnessed separately by a triangle and by every nontrivial higher
cube.

### Theorem 7.1 (no faithful full-Markov quotient)

There is no quotient by \(\sim_{\rm full}\) on which both

1. the all-depth load vector, and
2. literal safe-de-Bruijn concatenation at marked ports

are well defined.

#### Proof

The load vector descends by the first part of (7.1).  If literal
concatenation also descended, Corollary 2.2 would force the port map to
factor through the quotient, equivalently
\(\mathcal L_{\rm full}\subseteq\ker\mathsf P\).  This contradicts the
second part of (7.1). \(\square\)

### Corollary 7.2 (the full Markov basis does not repair diagonal pairing)

The triangle Markov theorem for the common-template score fibre cannot
be used to contract that fibre to a network node and then recover
literal diagonal occurrence pairing.  A representative chosen after
the contraction need not accept the continuations chosen before the
contraction.

To use cycle or cube moves constructively, one must instead retain the
marked ports and solve a **marked-fibre routing problem**.  In the
fixed-core sector of Theorem 3.1 the marked fibre is a singleton, so the
unmarked triangle Markov theorem supplies no residual freedom at all.
With only a sparse set of marked component boundaries, some
port-avoiding moves can survive, but no theorem above says that they
connect the marked fibre.

## 8. Consequence for the constant-one program

The audited move library now has a complete local classification for
this proposed shortcut.

* Quartets, higher cubes, triangles, and longer cycle reversals are
  exact all-depth moves.
* With a common retained phase/tag schedule, they preserve the
  phase-run count and hence do not autonomously reduce the number of
  promotion paths.
* The full cycle library is a Markov basis for the unmarked fixed-core
  score fibre.
* That Markov equivalence is not compatible with literal safe-port
  concatenation.
* Every natural literal augmentation still has determinant
  \(2^{\Theta(m/H)}\) minors.

Thus the higher exchanges do not turn the diagonal port-pairing
polytope into a TU/network polytope and do not yield a bounded-component
tight-path cover by quotienting.  A surviving positive route must make
one of two genuinely new advances:

1. construct a marked-fibre routing theorem which tracks every changed
   port and crossing collar throughout the cycle/cube moves; or
2. introduce a physical component-splicing operation whose legality and
   cost are proved before any port identification.

Neither is supplied by the common-template Markov basis itself.

## 9. Dependency ledger

The safe de Bruijn formulation and the original determinant-two block
are in
`MATH_THEOREM_PROMOTION_TIGHT_PATH_DEBRUIJN_TU_AND_PORT_PAIRING_OBSTRUCTION_20260726.md`.
The independent-block determinant amplification and the quartet audit
are in
`MATH_THEOREM_SAFE_DEBRUIJN_QUARTET_CLOSURE_AND_EXPONENTIAL_DETERMINANT_OBSTRUCTION_20260726.md`.
The exact higher placeholder cube identity is in
`MATH_THEOREM_PROMOTION_ALL_DEPTH_HIGHER_CUBE_EXCHANGE_20260726.md`.
The tournament-score factorization, physical cycle reversals, and
triangle Markov theorem are in
`MATH_THEOREM_ALL_DEPTH_FRAME_TORIC_FIBRE_AND_QUARTET_MARKOV_OBSTRUCTION_20260726.md`.
