# Lane W: a finite `CAA_29` packet certificate with exact Hall score

Date: 2026-07-28

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  In particular `[1,12]_0=(2,13)_1`.

## 0. Verdict

For the five-parent (k=15) successor catalogue, `CAA_29` can be made a
literal finite certificate.  The certificate uses correlated unions of
alternating cycles, never independent component flips.  Every accepted
state carries:

* an exact one-cycle trace;
* the relative parity, genus, and full successor-cycle partition;
* exact residence and all (9949) upper witnesses; and
* a maximum compiler matching together with an equal-size vertex cover.

The progress coordinate is

\[
                   \mu(C):=\nu(G_C),                         \tag{0.1}
\]

not the number of previously declared successes.  Thus the only terminal
value is

\[
                   \mu(C)=16383.                              \tag{0.2}
\]

This choice completely closes the moving-deficiency loophole.  If a packet
has score increment (d=\mu(Q)-\mu(C)), then, simultaneously for **every**
target shore (A),

\[
 h_Q(A)-h_C(A)
 \ge g_C(A)-\delta(C)+d.                                      \tag{0.3}
\]

In particular, (d\ge1) is genuine all-shore Hall descent and cannot be a
relocation of the Hall-29 witness.

There is also an exact low-congestion encoding.  Type a packet by its
absolute symmetric-difference arc set

\[
                   D=E(C)\mathbin\triangle E(Q).              \tag{0.4}
\]

Given (Q) and (D), the predecessor is uniquely recovered by
(E(C)=E(Q)\triangle D).  Hence every packet-score type ((D,d)) has
backward congestion at most one.  The resulting entropy inequality is a
finite Laurent-polynomial inequality, stated in Theorem 6.1 below.

What is **not** proved is that the five-parent catalogue contains a selected
atlas satisfying that inequality.  In fact, if arbitrarily large correlated
packets are admitted, existence of such an atlas is equivalent to existence
of a terminal carrier: any terminal carrier is one giant alternating packet
away from the initial carrier.  Thus unrestricted `CAA_29` is a certificate
format, not an independent existence argument.  A non-tautological theorem
must prove the inequality for a restricted reusable packet library (for
example, a support bound or a bounded template catalogue), or an exact
finite search must produce a terminal carrier.

No Hall-zero carrier and no constant-one result is claimed here.

## 1. The five-parent finite state space

Put

\[
 X=\binom{[15]}8\cup\{\partial\},\qquad |X|=6436.              \tag{1.1}
\]

Let (f_0,\ldots,f_4) be the augmented successor cycles of

\[
 P, (1,12)P, (3,4)P, (10,11)P, (3,13)P.                  \tag{1.2}
\]

Duplicate arcs are identified.  Define

\[
 E_*:=\bigcup_{a=0}^4\{(x,f_a(x)):x\in X\}.                 \tag{1.3}
\]

A **five-parent successor factor** is a permutation (C:X\to X) with
((x,C(x))\in E_*) for every (x).  It is a **legal carrier** when:

1. (C) has one cycle;
2. deleting ∂ gives no forbidden residence word;
3. every upper target at depths (1\le q\le7) has a literal non-wrapping
   witness window.

The upper-witness universe has size

\[
 \sum_{q=1}^7\binom{15}{8+q}=9949.                           \tag{1.4}
\]

Let \(\Omega\) be the set of legal carriers.  It is finite, with the crude
bound

\[
                         |\Omega|\le5^{6436}.                 \tag{1.5}
\]

The compiler target and physical-cell shores have sizes

\[
 |\mathcal T|=16383,\qquad |\mathcal C|=19311.               \tag{1.6}
\]

For (C\in\Omega), let (G_C\) be its exact physical compiler graph and
set

\[
 \mu(C)=\nu(G_C),\qquad \delta(C)=16383-\mu(C).              \tag{1.7}
\]

Auxiliary witnesses are canonically chosen (for example,
lexicographically first), so they do not create extra mathematical states.

## 2. Exact construction of every correlated successor packet

Fix (C\in\Omega).  Its residual source digraph has, for every non-current
parent arc ((x,f_a(x))), the labelled arc

\[
              x\longrightarrow C^{-1}(f_a(x)).               \tag{2.1}
\]

There are at most four distinct non-loop choices at a source.  A directed
cycle

\[
 x_1\to x_2\to\cdots\to x_\ell\to x_1                   \tag{2.2}
\]

in this residual digraph prescribes the alternating switch

\[
 Q(x_i)=C(x_{i+1})\quad(1\le i\le\ell),                    \tag{2.3}
\]

with indices read cyclically.  A vertex-disjoint family of residual cycles
may be switched simultaneously.  This is a correlated packet; no assertion
is made that its constituent cycles may be switched independently while
remaining Hamilton.

### Lemma 2.1 (packet completeness)

For any two five-parent successor factors (C,Q), put

\[
                         \rho=C^{-1}Q.                        \tag{2.4}
\]

The nontrivial cycles of \(\rho\) are exactly the residual alternating
cycles switched in passing from (C) to (Q).  Consequently, enumeration
of vertex-disjoint residual-cycle families enumerates every correlated
packet endpoint in the five-parent union.

#### Proof

The identity (Q=C\rho) gives

\[
                         Q(x)=C(\rho(x)).                     \tag{2.5}
\]

Thus if ρ contains the cycle ((x_1\ldots x_\ell)), the new edge out of
(x_i) ends at (C(x_{i+1})).  Alternating this new edge with the reverse
of the old (C)-edge gives one bipartite alternating cycle of length
(2\ell).  Distinct ρ-cycles are vertex-disjoint.  Conversely, traversing
any symmetric-difference alternating cycle by a (Q)-edge followed by a
reverse (C)-edge gives the corresponding cycle of (C^{-1}Q). \(\square\)

This proves that the packet catalogue is finite and complete.  It does not
prove that a useful endpoint exists.

## 3. Exact parity, genus, and subtour state

For a packet (C\to Q), let

\[
 s(C,Q)=6436-c(C^{-1}Q)
       =\sum_{O}(|O|-1),                                      \tag{3.1}
\]

where the sum is over its nontrivial relative cycles.  Let
\(\Pi(Q)\) be the complete cycle partition of (Q).

### Lemma 3.1 (relative map ledger)

There is a nonnegative integer (g(C,Q)) satisfying

\[
 c(Q)=1+s(C,Q)-2g(C,Q).                                      \tag{3.2}
\]

Therefore

\[
 Q\text{ is Hamilton}
 \iff
 s(C,Q)\equiv0\pmod2,quad
 \Pi(Q)=\{X\},\quad
 g(C,Q)=s(C,Q)/2.                                            \tag{3.3}
\]

#### Proof

The permutations (C) and \(\rho=C^{-1}Q\) define a connected orientable
permutation map because (C) is transitive.  Euler's formula is

\[
 2-2g=c(C)+c(\rho)-6436+c(C\rho)
      =1+c(\rho)-6436+c(Q).
\]

Substitute (s=6436-c(\rho)) and rearrange.  Equation (3.3) follows.
\(\square\)

Thus a packet record contains the relative-cycle list, (s\bmod2), (g),
and \(\Pi(Q)\).  A one-cycle trace beginning at ∂ independently verifies
that \(\Pi(Q)=\{X\}\).  Tracking only the parity or only the number of
relative components is not a circuit certificate.

For partial packet enumeration, the exact state is still
((s\bmod2,g,\Pi)\); in particular, the full subtour partition, rather than
only its cardinality, is needed to know how a later residual cycle meets
the existing subtours.

## 4. Residence, upper, and exact compiler witnesses

The following data give a finite independently checkable state certificate.

1. **Successor provenance.**  For each source (x), give an index
   (a\in\{0,\ldots,4\}) with (C(x)=f_a(x)).  If several parents contain
   the same arc, use the least index.
2. **Hamilton trace.**  Give
   \(\partial,x_1,\ldots,x_{6435},\partial\), with the middle vertices
   pairwise distinct and every consecutive pair an arc of (C).
3. **Residence.**  For every member (F) of the finite forbidden
   residence-path catalogue, exhibit one arc of (F) absent from (C).
   Equivalently, a verifier may enumerate all length-two through length-four
   selected paths and compare them with that catalogue.
4. **Upper witnesses.**  For each of the (9949) upper targets, give one
   start position and depth whose non-wrapping consecutive window is a
   literal witness.
5. **Exact compiler score.**  Give a matching (M_C) in (G_C) and a
   vertex cover
   \[
       K_C=K_C^{\mathcal T}\mathbin\dot\cup K_C^{\mathcal C}
   \]
   with
   \[
                    |M_C|=|K_C|=\mu(C).                      \tag{4.1}
   \]

The last item proves μ exactly by weak duality and Kőnig's theorem.  In
particular, it is not enough to carry a matching declared to have the
current rollback level: an equal-size cover is what proves that the score
has not silently been underestimated.

### Lemma 4.1 (the vertex cover is a moving-DM certificate)

Put

\[
                  A_C=\mathcal T\setminus K_C^{\mathcal T}.   \tag{4.2}
\]

Then

\[
 N_C(A_C)=K_C^{\mathcal C},\qquad
 |A_C|-|N_C(A_C)|=\delta(C).                                 \tag{4.3}
\]

#### Proof

Because (K_C) covers every edge, every neighbour of a target outside
(K_C^{\mathcal T}) lies in (K_C^{\mathcal C}).  Hence

\[
 |A_C|-|N_C(A_C)|
 \ge 16383-|K_C^{\mathcal T}|-|K_C^{\mathcal C}|
 =16383-\mu(C)=\delta(C).
\]

Hall's deficiency formula and maximality of (M_C) give the reverse
inequality.  Equality follows, and it forces
(N_C(A_C)=K_C^{\mathcal C}). \(\square\)

Different minimum covers may expose different maximizing DM shores.  This
does not matter: equality (4.1) certifies the maximum over **all** shores.

### Theorem 4.2 (exact all-shore transition identity)

Let (C,Q\in\Omega), put (d=\mu(Q)-\mu(C)), and define

\[
 v_{C,Q}(A)=|N_Q(A)|-|N_C(A)|,qquad
 g_C(A)=|A|-|N_C(A)|.                                        \tag{4.4}
\]

Then, for every (A\subseteq\mathcal T),

\[
 \boxed{
 v_{C,Q}(A)\ge g_C(A)-\delta(C)+d.}                          \tag{4.5}
\]

Conversely, (4.5) for all (A) implies
μ(Q)≥μ(C)+d.

#### Proof

Since (g_Q(A)\le\delta(Q)=\delta(C)-d),

\[
 v_{C,Q}(A)=g_C(A)-g_Q(A)
 \ge g_C(A)-\delta(C)+d.
\]

Conversely, (4.5) says (g_Q(A)\le\delta(C)-d) for every (A).  Maximize
over (A) and use Hall's formula. \(\square\)

Thus exact matching-size gain is precisely the moving-DM/all-shore
certificate required to prevent relocation.  Frozen old DM families and
the seven old zero targets play no logical role in (4.5).

There is also an exact rollback ledger.  Retain from a maximum (M_C) the
edges still present in (G_Q):

\[
 M_0=M_C\cap E(G_Q),\qquad r=|M_C\setminus M_0|.              \tag{4.6}
\]

If α is the number of (M_0)-augmenting components in
(M_0\triangle M_Q), where (M_Q) is maximum in (G_Q), then

\[
                     d=\alpha-r.                              \tag{4.7}
\]

Indeed, every other symmetric-difference component is balanced, while an
(M_0)-augmenting component adds one edge.  Formula (4.7) makes compiler
damage, repair, and rollback agree exactly with the terminal score (0.1).

## 5. Unit backward congestion from absolute packet types

For a packet (C\to Q), define its absolute type

\[
                  D(C,Q)=E(C)\triangle E(Q).                  \tag{5.1}
\]

The type retains both shores of every alternating cycle but no arbitrary
ordering or orientation.

### Lemma 5.1 (unit-congestion decoder)

Fix an output (Q), a packet type (D), and a score increment (d).
There is at most one predecessor (C) satisfying

\[
 D(C,Q)=D,qquad \mu(Q)-\mu(C)=d.                             \tag{5.2}
\]

It is recovered by

\[
                         E(C)=E(Q)\triangle D.                 \tag{5.3}
\]

If a state is not allowed to use the same (D) in two different trial
slots, the backward congestion of the record type β=(D,d) is at most one.

#### Proof

Symmetric difference is an involution.  Equation (5.3) determines the
entire successor edge set of (C), hence (C) itself.  The remaining
conditions can reject this candidate but cannot create another one.
\(\square\)

This is an actual congestion theorem; it uses the physical labelled packet,
not only its number of cycles, support size, or parent-colour word.  Passing
to a coarser packet orbit is possible, but its congestion must then include
the number of absolute lifts.

## 6. Finite entropy certificate with score μ

Let \(\mathcal S\subseteq\Omega\) be a finite set of nonterminal states,
containing the Hall-29 initial state (C_0).  At every (C\in\mathcal S),
select exactly (R) distinct packet trials.  Each output is either:

* a legal terminal carrier (Q) with μ(Q)=16383; or
* a legal nonterminal carrier (Q\in\mathcal S), with record type
  \(β=(D,d)\), where (D=D(C,Q)) and
  (d=μ(Q)-μ(C)).

Let \(\mathfrak B\) be the set of nonterminal record types actually used.

### Theorem 6.1 (finite unit-congestion `CAA_29`)

If there is a rational (x>0) such that

\[
 \boxed{
             \sum_{(D,d)\in\mathfrak B}x^d<R,}               \tag{6.1}
\]

then a finite trial word starting at (C_0) reaches a legal terminal
carrier.  Every intermediate state is one Hamilton circuit, residence-safe,
upper-complete, and its rollback value is its exact compiler matching size.

#### Proof

Consider a length-(N) trial word which has not reached a terminal state.
Record its nonterminal packet-score types and its final state.  By Lemma
5.1, reading backward from the final state and one record type gives at most
one preceding state/trial pair.  Thus each record word and final state has
at most one history.

If the final score is (h), the sum of the recorded increments is
(h-μ(C_0)).  Put

\[
                         F(x)=\sum_{(D,d)\in\mathfrak B}x^d.
\]

The total number of record words with this increment is at most

\[
                         F(x)^N x^{\mu(C_0)-h}.                \tag{6.2}
\]

Therefore the number of failing input words is at most

\[
 F(x)^N
 \sum_{h=0}^{16382}
   |\{C\in\mathcal S:\mu(C)=h\}|x^{\mu(C_0)-h}.              \tag{6.3}
\]

The second factor is a fixed finite constant.  There are (R^N) input
words.  Under (6.1), the ratio of (6.3) to (R^N) tends to zero, so some
input word reaches a terminal state. \(\square\)

Strict rational inequality makes (6.1) a completely exact certificate:
all negative powers can be cleared by multiplying by a sufficiently large
power of the numerator and denominator of (x).

Theorem 6.1 remains true with congestion numbers (c_{D,d}) if duplicate
slots or coarser records are used, after replacing the left side by
∑c_{D,d}x^d.

## 7. The finite atlas-selection problem

Once a finite candidate state/packet catalogue has been generated, selection
of the certificate in Theorem 6.1 is a finite (0/1) problem.  For a fixed
rational (x) and integer (R), use:

* (u_C\in\{0,1\}) to declare a nonterminal state present;
* (y_{C,D}\in\{0,1\}) to select the packet trial (D) at (C);
* (z_{D,d}\in\{0,1\}) to declare that a nonterminal record type is used.

The exact constraints are

\[
 u_{C_0}=1,                                                    \tag{7.1}
\]

\[
 \sum_Dy_{C,D}=Ru_C                                           \tag{7.2}
\]

for every candidate state (C), together with:

1. (y_{C,D}\le u_C);
2. if (C\triangle D=Q) is nonterminal, then
   (y_{C,D}\le u_Q) and
   (y_{C,D}\le z_{D,\mu(Q)-\mu(C)});
3. if (C\triangle D) is terminal, no record variable is charged;
4. (y_{C,D}=0) unless the packet endpoint passes all checks in Sections
   3--4; and
5. after clearing denominators,
   \[
      \sum_{D,d}z_{D,d}x^d<R.                                \tag{7.3}
   \]

The state closure in item 2 is essential.  Omitting it would let a finite
certificate discard precisely the bad states reached by its own trials.

A useful restricted search introduces a support parameter

\[
 b(D)=\tfrac12|D|,                                            \tag{7.4}
\]

the number of changed successor arcs, and permits only (b(D)\le B).
For such a packet, the safe compiler-cell damage estimate is

\[
              |\text{changed cell shores}|\le30B+36.         \tag{7.5}
\]

The actual matching/current certificate (4.7), not (7.5), determines its
score increment.

The finite search can increase (B).  At (B=6436), packet enumeration is
complete by Lemma 2.1.  Small (B), or a bounded reusable template family,
is the regime in which an entropy theorem would provide information beyond
direct terminal search.

## 8. Exact moving-DM separation in a carrier search

For a proposed carrier (Q), compute (G_Q), a maximum matching (M_Q),
and an equal-size minimum vertex cover (K_Q).  These give μ(Q) and the
current maximizing shore

\[
              A_Q=\mathcal T\setminus K_Q^{\mathcal T}.       \tag{8.1}
\]

If a search asks for score at least (b) and finds μ(Q)<b, the exact
separating Hall inequality is

\[
              |N_{Q'}(A_Q)|
              \ge |A_Q|-(16383-b)                             \tag{8.2}

for the next candidate (Q').  The left side is the number of physical
cells whose reconstructed shore meets (A_Q).  It is therefore a finite
Boolean function of the literal local cell words and both endpoint collars.

If a later candidate moves the defect, its own matching/cover pair produces
a new shore and a new inequality.  Separation terminates because the
carrier and target-shore universes are finite.  At (b=16383), exhaustion
of this separation is exactly full Hall, not positivity of the old seven
zeros or slack on a frozen list of DM shores.

The other carrier constraints also have exact finite separation:

* degree one is checked directly on successor and predecessor arrays;
* a non-Hamilton permutation returns its complete subtour partition, and a
  directed cut through any proper subtour is a valid rejection certificate;
* a selected forbidden residence word is itself a rejection certificate;
* a missing upper target is itself a rejection certificate; and
* a compiler failure returns (8.1).

Thus an external finite search need only output the positive certificate in
Sections 3--6.  No trust in the search program or in a frozen cut list is
needed for the mathematical conclusion.

## 9. Unrestricted packets make `CAA_29` equivalent to the terminal search

### Proposition 9.1 (one-packet equivalence)

The following are equivalent.

1. The five-parent union contains a legal carrier (Q) with
   μ(Q)=16383.
2. There is an unrestricted correlated-packet `CAA_29` certificate from the
   initial Hall-29 carrier.
3. There is such a certificate with one initial state, one trial, and no
   nonterminal record types.

#### Proof

The implications (3\Rightarrow2\Rightarrow1) follow from certificate
soundness.  For (1\Rightarrow3), Lemma 2.1 decomposes
(C_0^{-1}Q) into a vertex-disjoint family of alternating cycles.  Switch
the whole family as one correlated packet.  Take

\[
 \mathcal S=\{C_0\},\qquad R=1,\qquad \mathfrak B=\varnothing.
\]

The unique trial goes directly to (Q), and (6.1) reads (0<1).
\(\square\)

This proposition is the exact conceptual boundary.  Global Hamilton
dependence is correctly respected, but allowing an arbitrary whole-factor
packet hides the original existence problem inside one trial.  The shortest
honest computational target is therefore the terminal carrier itself.  The
shortest honest theorem target is a support- or template-restricted atlas
satisfying (6.1).

## 10. Exact remaining lemma

For a fixed useful restriction (\mathscr D\) on packet supports (for
example (b(D)\le B\), with (B\ll6436), or a specified reusable family),
the remaining positive statement is:

> **`FCAA_29(\mathscr D)`.** There exist a finite closed state set
> \(\mathcal S\ni C_0\), an integer (R\ge1), and a rational (x>0),
> together with (R) distinct legal packet trials from every state, all
> using supports in \(\mathscr D\), such that terminal trials or closure
> holds and
> \[
>             \sum_{(D,d)\text{ used nonterminally}}x^d<R.
> \]

Every state and packet must carry the certificates in Sections 3--4.
Theorem 6.1 then proves a Hall-zero five-parent carrier.

The currently frozen transposition counts, Pareto score, old-DM slacks, and
seven old zero multiplicities give no bound on the Laurent sum in this
lemma.  They do not determine:

* which alternating-cycle bundles attain maximum genus;
* which of those endpoints remain residence-safe and upper-complete;
* their exact matching currents α-r; or
* how many absolute packet types can be reused across states.

Accordingly, no numerical `FCAA_29` bound follows from the audited data now
available.  What has been proved is a finite complete packet generator, an
exact unit-congestion decoder, a relocation-proof rollback score, and an
independently verifiable certificate format.  A terminal carrier search, or
a genuinely new structural bound for a restricted packet library, remains
necessary.
