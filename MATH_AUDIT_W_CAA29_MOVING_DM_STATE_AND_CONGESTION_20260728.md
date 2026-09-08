# Audit of `CAA_29`: moving-DM state, exact compiler rank, and reverse congestion

Date: 2026-07-28

Scope: the five-parent (k=15) successor catalogue

\[
 \mathcal P_*=
 \{P_{29},(1,12)P_{29},(3,4)P_{29},(10,11)P_{29},(3,13)P_{29}\}.
\]

No finite search is performed in this note.  The purpose is to make the
proposed causal augmentation atlas finite and logically exact, and to audit
which compression of its state is permitted.

## 0. Verdict

Compiler matching size is an exact terminal value, but it is not by itself
an adequate causal state.

* If the level is the **maximum** compiler matching number, then a one-level
  increase is exactly the moving-DM/all-shore descent condition.  It cannot
  merely relocate a deficiency.
* If the level is only the size of an arbitrarily chosen carried matching,
  then reaching level (16383) is still conclusive, but intermediate levels
  neither identify the moving DM shore nor determine rollback length.
* An exact, finite, polynomially checkable state is obtained by making every
  auxiliary choice canonical and carrying a matching--vertex-cover pair of
  equal size.  The pair certifies the maximum matching number by König's
  theorem.
* The entropy inequality in the current formulation of `CAA_29` needs one
  correction.  If there are several success record types, the success term
  is (A_+x), not (x), where (A_+) is their total backward congestion.
  Conditional recoverability after the success type is supplied does not
  make (A_+=1).
* Parity, genus, and the number of subtours are exact audits but are not a
  Markov state for later packets.  The complete successor permutation (or
  equivalently its oriented cycle words) must remain in the state.

Thus a finite certificate search is well-defined after the corrections in
Sections 3--6 below.  No low-congestion bound for the actual five-parent
atlas follows from the current parent screens.  In particular, the unique
Pareto transposition and the seven positive old targets do not supply the
missing reverse-congestion inequality.

## 1. Exact compiler-rank potential

Let

\[
 N=16383,
 \qquad b=16354,
 \qquad D=N-b=29.
\]

For a legal carrier (C), let (G_C=(\mathcal T,\mathcal C;E_C)) be its
full physical compiler graph and put

\[
 \mu(C)=\nu(G_C),
 \qquad
 \delta(C)=N-\mu(C).
\tag{1.1}
\]

Here legality means one dummy-closed Hamilton circuit, exact depth-three
residence, and all upper targets through depth seven.

### Theorem 1.1 (primal--dual compiler-rank certificate)

For every legal carrier (C):

1. a matching (M_C) and a vertex cover (K_C) satisfying
   
   \[
      |M_C|=|K_C|=s
   \tag{1.2}
   \]
   
   certify (mu(C)=s);
2. (mu(C)=N) if and only if (C) has full compiler Hall;
3. if (C,Q) are legal and (d=\delta(C)), then the following are
   equivalent:
   
   \[
      \mu(Q)\ge \mu(C)+1,
   \tag{1.3}
   \]
   
   \[
      |N_{G_Q}(A)|\ge |A|-(d-1)
      \quad\hbox{for every }A\subseteq\mathcal T,
   \tag{1.4}
   \]
   
   and
   
   \[
      v_{C,Q}(A)
      \ge g_C(A)-d+1
      \quad\hbox{for every }A\subseteq\mathcal T,
   \tag{1.5}
   \]
   
   where
   
   \[
      g_C(A)=|A|-|N_{G_C}(A)|,
      \qquad
      v_{C,Q}(A)=|N_{G_Q}(A)|-|N_{G_C}(A)|.
   \]

#### Proof

Weak duality gives (|M_C|\le |K_C|) for every matching and every vertex
cover.  Equality in (1.2) therefore makes both optimal.  This proves the
first assertion.  The second is the defect form of Hall's theorem.

For the third assertion, Hall deficiency gives

\[
 \mu(Q)\ge N-(d-1)
 \iff
 \max_A\bigl(|A|-|N_{G_Q}(A)|\bigr)\le d-1.
\]

This is (1.4).  Substituting

\[
 |A|-|N_{G_Q}(A)|=g_C(A)-v_{C,Q}(A)
\]

gives (1.5). \(square\)

Consequently an atlas trial is protected against deficiency relocation if
it is accepted as a success only after one of the following literal
certificates is supplied:

* a matching in (G_Q) of size (mu(C)+1);
* the protected-collar augmenting certificate producing that matching; or
* the full moving-DM inequalities (1.5).

The first is normally the shortest certificate.  If the new level is
claimed to be the exact value (mu(Q)-b), then a same-size vertex cover is
also required.  Positivity of the seven old zero targets, or improvement of
any fixed collection of old DM shores, is not a substitute.

At level (h), where (mu(C)=b+h), condition (1.4) is

\[
 |N_{G_Q}(A)|\ge |A|-(28-h)
 \quad(A\subseteq\mathcal T).
\tag{1.6}
\]

At h = 28 this becomes the ordinary Hall inequality on every shore for the
successful output.  Level h = 29 is already terminal, so no further-success
inequality is imposed there.

## 2. Why the scalar alone is not a causal state

Let the target shore be ({1,2}) and the cell shore be ({a,b}).  In
(G_0), let both cells accept only target (1).  In (G_1), let both
cells accept only target (2).  Both graphs have maximum matching number
one.  Their unique maximal deficient directions are opposite.  An incidence
from target (2) to cell (a) augments (G_0) but does not augment
(G_1).

Thus the integer (mu=1) does not determine whether a proposed action is
a success.  More generally, relabelling a Hall-29 carrier preserves
(mu=16354) while transporting the entire maximum-deficiency lattice.
This is the exact deficiency-relocation phenomenon.

There is no contradiction with Theorem 1.1.  The level may be the scalar
(mu(C)-b), but the configuration must still retain (C), hence its full
compiler graph, or an equivalent primal--dual certificate.  A state space
whose configurations are only the integers (0,\ldots,29) is not a
`CAA_29` state space.

One may instead carry an arbitrary matching (M) and use (|M|-b) as the
level.  Every successful trial must then construct an actual larger
matching in the new compiler graph.  This is logically sufficient because
level 29 is a saturating matching.  It has two disadvantages:

1. the level need not equal (N-\delta(C)-b), so rollback length is not the
   change of the moving-DM potential; and
2. treating all choices of (M) as distinct configurations can create
   large artificial reverse congestion.

The second point is quantified next.

## 3. Canonicalization and the flag-volume obstruction

Fix total orders on successor arcs, compiler edges, physical upper windows,
and targets.  For every legal (C), define deterministically:

* (widehat M(C)), the first maximum compiler matching;
* (widehat K(C)), the first minimum compiler vertex cover; and
* (widehat W(C)), the first literal upper witness for every upper target.

The **canonical state** associated with (C) is

\[
 \widehat q(C)=
 (C,\widehat M(C),\widehat K(C),\widehat W(C)).
\tag{3.1}
\]

All auxiliary entries in (3.1) are functions of (C); they do not create
parallel copies of the same physical carrier.  They are finite and
checkable by repeated bipartite matching and finite window tests.  The level
is exactly

\[
 h(C)=\mu(C)-b.
\tag{3.2}
\]

Canonicalization is not cosmetic.  The following counting obstruction
holds for every causal atlas.

### Lemma 3.1 (success-volume cut)

Let (\mathcal Q_h,\mathcal Q_{h+1}) be two consecutive state levels.
Suppose every state in (\mathcal Q_h) has at least (s_h) successful
trial labels.  Let (\mathfrak S) be the success record types and let
(c_\beta) be the backward congestion of type (beta).  Put

\[
 A_+=\sum_{\beta\in\mathfrak S}c_\beta.
\tag{3.3}
\]

Then

\[
 \boxed{
 s_h|\mathcal Q_h|
 \le A_+|\mathcal Q_{h+1}|.}
\tag{3.4}
\]

#### Proof

Count successful predecessor-state/trial pairs.  There are at least
(s_h|\mathcal Q_h|).  For a fixed output state and a fixed type (beta),
there are at most (c_\beta) such pairs.  Summing over output states and
types gives the right side of (3.4). \(square\)

For a concrete illustration, let the compiler graph be (K_{N,N}), and
let configurations distinguish every matching of the displayed size.  The
number of size-(s) matchings is

\[
 m_s=\binom Ns^2s!.
\tag{3.5}
\]

Hence

\[
 \frac{m_{N-1}}{m_N}=N.
\tag{3.6}
\]

If every size-(N-1) matching state has even one success, (3.4) forces
(A_+\ge N).  Thus no general low-congestion theorem can be based on the
phrase “carry some matching of the required size.”  The same multiplicity
problem occurs if every choice of an upper witness is made a separate
configuration.

There are two legitimate repairs:

1. use the canonical state (3.1); or
2. use a history-decorated state in which the newly installed packet is
   self-identifying and popping it recovers the predecessor.

The second choice does not remove the burden: every rollback which erases a
history tail must encode that tail with its true congestion.  The first is
the smaller finite certificate space and is the recommended `CAA_29`
normal form.

## 4. Correction to the entropy polynomial

Suppose all success symbols have increment (+1), and failure symbols of
rollback length (ell) have increment (1-ell).  Define

\[
 A_+=\sum_{\beta\in\mathfrak S}c_\beta,
 \qquad
 A_\ell=\sum_{\beta\in\mathfrak B_\ell}c_\beta.
\tag{4.1}
\]

The record polynomial in the finite rollback theorem is

\[
 \boxed{
 F(x)=A_+x+\sum_{\ell\ge1}A_\ell x^{1-\ell}.}
\tag{4.2}
\]

Therefore the correct threshold is

\[
R>\inf_{x>0}F(x).
\tag{4.3}
\]

If only rollback lengths one and two occur, then

\[
 F(x)=A_+x+A_1+A_2/x
\]

and minimization gives the exact corrected threshold

\[
 \boxed{R>A_1+2\sqrt{A_+A_2}.}
\tag{4.3a}
\]

This follows directly by grouping the record symbols in the polynomial
(sum_\beta c_\beta x^{d_\beta}).  In particular, the term (x) used in
the current statement of `CAA_29` is valid only if

\[
 \sum_{\beta\in\mathfrak S}c_\beta=1.
\tag{4.4}
\]

Because the congestions are positive integers for nonempty types, (4.4)
means that there is one success record of congestion one.  Equivalently,
after forgetting the trial label, the combined success map

\[
 (\hbox{predecessor state},\hbox{trial})
 \longmapsto
 \hbox{output state}
\tag{4.5}
\]

must be injective.  The weaker assertion

> the predecessor and trial are recoverable from the output **and the
> success type**

only proves (c_\beta=1) separately.  With (k) nonempty success types it
gives (A_+=k), not one.

Packet labels cannot be hidden in the record for free.  If every packet is
made its own success type, then its count appears in (A_+).  To retain the
coefficient one, the chosen packet must be self-identifying from the output
canonical state, or the state must carry a reversible installed-packet
stack.

## 5. Exact topology state: parity and genus are not enough

Let (C) be the current dummy-closed Hamilton successor permutation on
(n=6436) owners, and let (Q) be a candidate successor permutation.
Put

\[
 \rho=C^{-1}Q,
 \qquad
 s=n-c(\rho).
\tag{5.1}
\]

The connected permutation-map formula gives an integer (g\ge0) such that

\[
 c(Q)=1+s-2g.
\tag{5.2}
\]

Thus the exact packet audit is

\[
 Q\text{ Hamilton}
 \iff
 s\equiv0\pmod2
 \text{ and }g=s/2.
\tag{5.3}
\]

This formula applies to an arbitrary relative permutation rho, not only to
a two-parent overlay.  It is a useful independent certificate.
However, the scalars parity, (g), and (c(Q)) are not sufficient state
for a subsequent packet.

### Proposition 5.1 (non-Markov topology summary)

There are two states having the same relative parity, genus, and subtour
count for which the same next transposition is Hamilton-making in one state
and subtour-splitting in the other.

#### Proof

On six symbols let

\[
 f=(1\ 2\ 3\ 4\ 5\ 6),
 \qquad
 h_1=(1\ 2\ 3)(4\ 5\ 6),
 \qquad
 h_2=fh_1f^{-1}=(2\ 3\ 4)(5\ 6\ 1).
\tag{5.4}
\]

The relative permutations (f^{-1}h_1) and (f^{-1}h_2) are conjugate:

\[
 f^{-1}h_2=h_1f^{-1}
 =f(f^{-1}h_1)f^{-1}.
\]

They therefore have the same number of cycles and the same (s).  Both
(h_i) have two cycles, so (5.2) gives the same genus and parity.

Now right-multiply by the transposition tau = (1 2).  In h_1, symbols 1 and
2 lie in the same cycle, so h_1 tau splits that cycle and has three cycles.
In h_2, symbols 1 and 2 lie in different cycles, so h_2 tau merges the two
cycles and h_2 tau is Hamilton.

Accordingly an exact finite atlas must store the full successor permutation
(C), or equivalently all oriented cycle words.  If a packet is assembled
incrementally, it must store the full partial path/cycle partition and its
exposed ends.  A parity bit, genus value, and subtour count are valid
prefilters but not rollback state.

When complete candidate successors are generated atomically, no exponential
subtour list is needed: traversing (Q) once decides whether it is one
cycle.  Residence is decided by the exact last-three-insertions automaton,
and upper coverage by the finite list of 9949 targets.  The apparent global
conditions are therefore finite and directly testable; only the atlas
expansion/congestion bound remains mathematical.

## 6. A finite, relocation-proof `CAA_29` certificate format

Let (\Omega_h) be the canonical states (3.1) whose carriers use only arcs
from the five parents, are Hamilton, resident and upper-complete, and obey

\[
 \mu(C)=b+h.
\tag{6.1}
\]

A packet record from (C) consists of a changed-source set (S), the new
parent-labelled successors on (S), and a finite record class (beta).
It determines (Q) literally.  The verifier performs the following tests.

1. **Degree:** the selected successors form a permutation and every arc is
   in the five-parent union.
2. **Circuit:** compute rho = C^{-1}Q, s, g, and the exact cycle
   decomposition of (Q); require one cycle.
3. **Residence:** cut at the dummy and run the depth-three queue automaton.
4. **Upper:** verify all 9949 literal upper targets; then replace witness
   choices by the canonical list (widehat W(Q)).
5. **Compiler:** build (G_Q), and verify the canonical matching--cover
   pair.  A success requires
   
   \[
       \mu(Q)\ge\mu(C)+1.
   \tag{6.2}
   \]
   
   By Theorem 1.1 this is exactly the moving-DM/all-shore certificate and
   cannot relocate equal deficiency.
6. **Rollback:** assign the exact increment
   
   \[
      d=\mu(Q)-\mu(C)
   \tag{6.3}
   \]
   
   and its record class.  Candidates with (mu(Q)<b) must either be
   excluded or the level range must be enlarged; clipping them to level zero
   is not an exact rollback encoding.
7. **Congestion:** for each output canonical state (Q) and record class
   (beta), count
   
   \[
      c_\beta(Q)=
      \#\{(C,\text{trial}):C\xrightarrow{\text{trial}}Q,
          \ \text{record}=\beta\},
   \tag{6.4}
   \]
   
   and certify
   
   \[
      c_\beta=\max_Qc_\beta(Q).
   \tag{6.5}
   \]

The resulting finite atlas is valid exactly when every nonterminal
canonical state has the prescribed (R) trials and the corrected
polynomial (4.2) satisfies (4.3).  The tables (6.4)--(6.5), rather than raw
packet multiplicities at the input, are the low-congestion certificate.

This format also gives an exact finite obstruction.  Failure of a trial can
be classified as degree, circuit, residence, upper, compiler rank, or
reverse-collision.  A state with no trial satisfying (6.2) is a literal
moving-DM sink in the five-parent legal carrier space.  A family satisfying
(6.2) but violating (3.4) or (4.3) is a literal reverse-volume obstruction
to this entropy-compression scheme.

## 7. Proved and unproved boundary

The following points are now rigorous.

1. Maximum compiler matching number is a valid terminal and rollback
   potential.
2. A strict increase in that number is exactly the all-shore/moving-DM
   inequality, so accepted successes cannot merely move the Hall-29 block.
3. A matching--vertex-cover equality is a short exact certificate of the
   level.
4. Arbitrary matching and upper-witness flags must be canonicalized or paid
   for in reverse congestion.
5. The success coefficient in the entropy polynomial is (A_+), not
   automatically one.
6. Exact circuit verification requires the full successor permutation;
   parity/genus/subtour scalars alone are not a sufficient dynamic state.
7. The corrected atlas and every one of its congestion constants are finite
   and testable by (6.1)--(6.5).

What remains unproved is the substantive `CAA_29` bound: the actual
five-parent legal carrier space must contain, from every reachable
nonterminal canonical state, enough packets of positive compiler-rank
increment, with output fibres small enough to satisfy (4.3).  None of the
known parent-pure count vectors, old-shore slacks, or Pareto diagnostics
implies this.  A finite certificate search must therefore optimize the
exact maximum matching number and tabulate the true output fibres; a search
which only clears the seven old zero targets can certify a relocated
Hall-29 state and is not a `CAA_29` search.
