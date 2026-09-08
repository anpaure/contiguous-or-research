# All-form one-chip voltage packets and the exact deletion-code gate

Date: 2026-07-26

> **Post-audit correction.**  The packet construction, voltage theorem,
> degree formula, phase resolution, and half-cover remain valid.  The
> proposed near-perfect matching gate is impossible: every packet matching
> covers at most \((1/2+o(1))T\) odd form classes, and the phase matching is
> asymptotically sharp.  See
> `MATH_AUDIT_ONE_CHIP_PACKETS_VS_DELETION_CODES_20260726.md`, especially
> the dual-shadow Theorem 5.4.  In particular, the statements below that a
> near-perfect or perfect packet matching remains open are superseded.

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 T={W\over n}=\operatorname {Cat}_m.
\tag{0.1}
\]

There is an exact all-form packet system which removes both defects of the
published awesome-form construction:

* every circular-gap form, including every non-good form, is incident with
  at least one packet; and
* every packet has unit voltage for every odd \(n=2m+1\), prime or
  composite.

The construction is elementary.  A rooted odd-central form is a positive
composition

\[
                         d=(d_1,\ldots,d_m),\qquad
                         \sum_i d_i=2m+1.
\tag{0.2}
\]

When \(d_m\ge2\), apply the one-chip successor

\[
 \Phi(d_1,\ldots,d_m)
 =(d_2,\ldots,d_{m-1},d_m-1,d_1+1).
\tag{0.3}
\]

After lowering the last part by one, (0.3) is just cyclic rotation of a
positive composition of \(2m\).  Hence every even-central circular form
\(z\) of least period \(r\mid m\) supplies a quotient Euler packet
\(P(z)\) of exactly \(r\) distinct odd-central form classes.  Its total
voltage is

\[
                         v(P(z))=2r\pmod {2m+1}.
\tag{0.4}
\]

Since \(r\mid m\),

\[
                         \gcd(2m+1,2r)=1.
\tag{0.5}
\]

Thus the physical lift of \(P(z)\) is **one** singleton-Ucycle component
of length \((2m+1)r\).  Periodic parents cause shorter packets, but never
voltage splitting.

The packets have an exact \(m\)-phase resolution.  Define

\[
                         \kappa(d)=\sum_{i=1}^m i d_i\pmod m.
\tag{0.6}
\]

Cyclic rotation changes \(\kappa\) by \(-1\), whereas \(\Phi\) preserves
\(\kappa\).  Therefore packets having one fixed \(\kappa\)-phase are
pairwise form-disjoint.  The largest phase covers at least

\[
                         {m+1\over2m}T
\tag{0.7}
\]

form classes and, apart from exponentially few periodic packets, uses only

\[
                         O(T/m)=O(W/m^2)
\tag{0.8}
\]

physical Ucycle components.  This is a rigorous coefficient-one
half-cover, and it includes whatever bad classes occur in that phase.

The exact all-form problem is now a concrete matching problem, not an
unspecified extension of the CHHM catalogue.  Form the hypergraph
\(\mathcal H_m\) whose vertices are odd-central form classes and whose
edges are the packets \(P(z)\).  Then an aperiodic matching covering
\(T-o(T)\) vertices gives \((1+o(1))T/m=O(W/m^2)\) unit-voltage
components on those forms.  An exact packet decomposition is precisely a
perfect matching of \(\mathcal H_m\).  Equivalently, in binary language it
is a cyclic constant-weight single-zero-deletion perfect code.

This matching is not proved below.  The phase resolution supplies \(m\)
explicit matchings whose average covered mass is asymptotically one half
of the vertices, so at least one has that coverage.  Combining packets
from different phases without owner overlap is the remaining integral
discrepancy.  Thus the note advances the previous audit in two
ways:

1. it gives legal options for **all** bad forms and makes every packet's
   composite voltage a unit; and
2. it isolates the exact finite matching object whose near-perfect or
   perfect resolution would prove the requested component bound.

Lower-prefix coverage has an equally explicit incidence form.  If
\(z=(z_1,\ldots,z_r)\) is periodically extended and \(q\ge1\), the
depth-\(q\) prefix emitted at packet phase \(t\) is the translation orbit
of

\[
 \left\{0,z_{t+1},z_{t+1}+z_{t+2},\ldots,
              z_{t+1}+\cdots+z_{t+m-q-1}\right\}\pmod n.
\tag{0.9}
\]

Consequently prefix coverage is one further family of orbit-incidence
inequalities imposed on the **same** packet matching.  The marginal
supply/demand ratio at \(q=A\sqrt m\) is \(e^{A^2+o(1)}\), and composite
target stabilizers are exponentially sparse.  A subsequent compatibility
audit shows that this scalar ratio is misleading: every emitted
depth-\(q\) target has a circular gap at least \(q+2\), whereas a
\(1-o(1)\) proportion of Gaussian-depth targets has no such gap.  Thus the
consecutive-prefix augmentation has a linear zero-degree Hall cut even
though its total occurrence count has slack.  See
`MATH_AUDIT_ONE_CHIP_INSERTION_SPHERE_MATCHING_AND_GAUSSIAN_PREFIX_NOGO_20260726.md`.

## 1. The exact quotient overlap graph

Let \(\mathcal C_{N,m}^+\) be the positive compositions of \(N\) into
\(m\) parts.  Let \(R\) denote left cyclic rotation.

For \(n=2m+1\), the action of \(R\) on \(\mathcal C_{n,m}^+\) is free.
Indeed, if a word were \(k>1\) repetitions of a shorter word, then
\(k\mid m\) and \(k\mid n\), contradicting \(\gcd(m,n)=1\).  Thus the
odd-central form set is

\[
 \mathcal F_m=\mathcal C_{2m+1,m}^+/\langle R\rangle,
 \qquad |\mathcal F_m|={1\over m}\binom{2m}{m-1}=T.
\tag{1.1}
\]

There is a useful literal quotient de Bruijn graph.  Its states are the
positive \((m-2)\)-tuples whose sum is at most \(n-2\).  A rooted
composition \(d\) is the directed edge

\[
 (d_1,\ldots,d_{m-2})\longrightarrow
 (d_2,\ldots,d_{m-1}).
\tag{1.2}
\]

The physical representative begins with the symbol \(0\) and then adds
the successive gaps \(d_1,d_2,\ldots\).  Therefore the translation voltage
of (1.2) is

\[
                         \nu(d)=d_1\pmod n.
\tag{1.3}
\]

The \(m\) rootings of one form are the \(m\) possible colored edges
associated with that form.  Selecting one rooted edge from every form and
balancing (1.2) is exactly the all-form colored Euler-circulation problem.

Two rooted forms can be consecutive precisely when

\[
 d'=(d_2,\ldots,d_{m-1},x,y),qquad
                         x+y=d_1+d_m,\quad x,y\ge1.
\tag{1.4}
\]

Thus the only local operation is to repartition the two boundary gaps.
The one-chip map (0.3) is the choice \(x=d_m-1\), \(y=d_1+1\).

## 2. The one-chip packet theorem

Let

\[
                         \mathcal B_m=
                  \mathcal C_{2m,m}^+/\langle R\rangle
\tag{2.1}
\]

be the even-central parent forms.  A member may have a nontrivial rotation
stabilizer.  Write \(r(z)\mid m\) for its least period.

For a rooted \(z=(z_1,\ldots,z_m)\), put

\[
                         \iota(z)=(z_1,\ldots,z_{m-1},z_m+1).
\tag{2.2}
\]

Then

\[
                         \Phi(\iota(z))=\iota(Rz).
\tag{2.3}
\]

### Theorem 2.1 (all-form one-chip packets)

For every \([z]\in\mathcal B_m\), the orbit

\[
 P(z)=\bigl(e(\iota(z)),e(\iota(Rz)),\ldots,
                  e(\iota(R^{r(z)-1}z))\bigr)
\tag{2.4}
\]

is a directed quotient Euler circuit in (1.2), where \(e(d)\) denotes the
rooted edge (1.2).  The colours
\([\iota(R^tz)]\), \(0\le t<r(z)\), are \(r(z)\) distinct odd form
classes.  Its total voltage is \(2r(z)\), a unit modulo \(2m+1\).
Hence its complete physical lift is one singleton-Ucycle component of
length \((2m+1)r(z)\).

#### Proof

Equation (2.3), together with (1.2), proves consecutive state agreement,
so (2.4) is a directed quotient circuit.

For distinctness, use the phase \(\kappa\) from (0.6).  Direct calculation
gives

\[
 \kappa(Rd)-\kappa(d)
 =m d_1-\sum_i d_i
 \equiv-1\pmod m
\tag{2.5}
\]

for every odd-central \(d\), while

\[
                         \kappa(\Phi(d))=\kappa(d)\pmod m.
\tag{2.6}
\]

If two rooted members of the \(\Phi\)-orbit represented the same odd
form, one would be a rotation of the other.  Equations (2.5)--(2.6) force
that rotation to be zero modulo \(m\), so the rooted members themselves
are equal.  The orbit length is therefore exactly \(r(z)\), and its form
classes are distinct.

During one least-period traversal, the first gaps emitted in (1.3) are one
period of \(z\).  Since \(z\) consists of \(m/r\) repetitions and has
total sum \(2m\), that period has sum

\[
                         {2m\over m/r}=2r.
\tag{2.7}
\]

This is the total voltage.  Since \(r\mid m\), any divisor of \(2m+1\)
and \(2r\) also divides \(m\); it is therefore one.  The standard voltage
lift of a length-\(r\) circuit with unit voltage has one component of
length \(nr\). \(\square\)

The theorem applies without asking whether the child forms are good,
awesome, or bad.  Every odd-central form has at least one part at least
two, because its \(m\) positive parts sum to \(2m+1\).  Lowering any such
part supplies an incident parent packet.

## 3. Exact degrees, phases, and exceptional periodic parents

Let \(F=[d]\in\mathcal F_m\), and define

\[
                         s(F)=|\{i:d_i\ge2\}|.
\tag{3.1}
\]

This is rotation invariant.

### Proposition 3.1 (vertex degree)

The degree of \(F\) in the packet hypergraph \(\mathcal H_m\) is exactly
\(s(F)\).

#### Proof

Every position with \(d_i\ge2\) may be rotated to the last position and
lowered by one, producing a parent packet containing \(F\).  If two such
active roots produced the same packet, they would occur twice on the same
\(\Phi\)-orbit.  The phase argument in Theorem 2.1 would then force the two
roots to coincide.  Thus the parents are distinct. \(\square\)

Writing \(d_i=1+y_i\), the vector \(y\) is a weak composition of \(m+1\)
into \(m\) parts.  The number of form vertices of degree \(s\) is exactly

\[
                         V_s={1\over m}
                         \binom ms\binom m{s-1}.
\tag{3.2}
\]

Indeed choose the \(s\) positive coordinates of \(y\), then a positive
composition of \(m+1\) into those coordinates, and divide by the free
rotation orbit size \(m\).  In particular,

\[
 \sum_sV_s=T,qquad
 \sum_s sV_s=\binom{2m-1}{m-1}={m+1\over2}T.
\tag{3.3}
\]

Thus the average packet degree is exactly \((m+1)/2\).  Formula (3.2) is
the Narayana distribution and is exponentially concentrated away from
the linear tails \(|s-m/2|>\varepsilon m\).

Every packet has the constant phase

\[
                         a(P)=\kappa(\iota(z))\in\mathbb Z_m.
\tag{3.4}
\]

### Proposition 3.2 (exact phase resolution)

For every \(a\in\mathbb Z_m\), the packets with \(a(P)=a\) are pairwise
vertex-disjoint.  Across the \(m\) phase matchings, a form \(F\) occurs
in exactly \(s(F)\) of them.

#### Proof

Suppose two phase-\(a\) packets meet at \(F\).  Their incidences choose two
rootings of \(F\) having phase \(a\).  Equation (2.5) says the \(m\)
rootings of \(F\) have all \(m\) different phases.  Hence the roots are
equal; lowering their last part gives the same parent, so the packets are
equal.  Proposition 3.1 gives the last assertion. \(\square\)

Summing the sizes of the phase matchings and using (3.3), some phase covers
at least

\[
                         {1\over m}\sum_Fs(F)
                         ={m+1\over2m}T
\tag{3.5}
\]

vertices.  This proves (0.7).

The periodic parents are negligible.  If \(z\) has least period
\(r<m\), then \(r\mid m\) and its period block is a positive composition
of \(2r\) into \(r\) parts.  Therefore their total number is at most

\[
 \sum_{\substack{r\mid m\\r<m}}\binom{2r-1}{r-1}
 \le 2^{m+o(m)}=e^{-\Omega(m)}T.
\tag{3.6}
\]

The same estimate, multiplied by \(m\), bounds all vertices lying in
periodic packets.  Hence the phase matching in (3.5) uses

\[
 {1\over m}\left({m+1\over2m}T+o(T)\right)+o(T/m)
 =O(T/m)
\tag{3.7}
\]

packets: every nonexceptional one has size \(m\).  Theorem 2.1 turns them
into the same number of physical Ucycle components.

## 4. Binary deletion-code interpretation

A positive composition \(z\) of \(2m\) into \(m\) parts is the cyclic gap
word of a balanced binary necklace of length \(2m\) and weight \(m\).
Increasing one part inserts one additional zero in the corresponding
cyclic gap.  Hence

\[
 P(z)=\{\text{odd necklaces obtained from }z
                \text{ by one cyclic zero insertion}\}.
\tag{4.1}
\]

Theorem 2.1 says these insertion spheres are not merely set packets: their
cyclic order is a legal unit-voltage Euler circuit.

Consequently:

### Theorem 4.1 (exact component/matching equivalence)

Let \(\mathcal M\subseteq\mathcal B_m\).  The packet lifts indexed by
\(\mathcal M\) are owner-disjoint if and only if their cyclic zero-insertion
spheres are disjoint.  They cover every odd-central form exactly once if
and only if \(\mathcal M\) is a perfect matching of \(\mathcal H_m\), or
equivalently a perfect cyclic constant-weight single-zero-deletion code.

If \(\mathcal M\) consists of aperiodic parents and leaves \(L\) form
vertices uncovered, then

\[
                         |\mathcal M|={T-L\over m}.
\tag{4.2}
\]

Thus a near-perfect matching with \(L=o(T)\) gives

\[
                         |\mathcal M|=(1+o(1)){T\over m}
                         =O(W/m^2)
\tag{4.3}
\]

unit-voltage components on all covered forms.

The distinction between near-perfect and exact is material.  Appending the
\(nL=o(W)\) missed physical owners literally is sufficient for a
coefficient-one OR word, but it is not a decomposition of *all* owners into
singleton-Ucycle components.  A pure all-form Ucycle factor needs either a
perfect packet matching or a legal Euler absorber for the residual forms.

The phase resolution proves a matching covering asymptotically one half of
the vertices, but does not prove a near-perfect matching.  Indeed, a packet
from a second phase normally meets many packets of the first phase.  Taking
several phase matchings independently is invalid.

The exact remaining integral discrepancy may be written as

\[
 \boxed{
 \max\left\{\sum_{P\in\mathcal B_m}|P|x_P:
       \sum_{P\ni F}x_P\le1\ (F\in\mathcal F_m),\quad
       x_P\in\{0,1\}\right\}=T-o(T).}
\tag{4.4}
\]

The desired exact packet factor replaces the right side by \(T\).
Equations (3.2)--(3.6) show that bad classes, low degree tails, and periodic
parents do not create a positive-density scalar deficit.  What is not yet
proved is the all-set weighted matching cut for (4.4).  Degree and ordinary
pair-codegree estimates alone cannot establish it at packet rank
\(m\), because projective-plane hypergraphs show that such a growing-rank
inference is false in general.

## 5. Exact lower-prefix incidence

Fix a parent \(z\) of period \(r\), extend it periodically, and orient the
packet as in (2.4).  At packet phase \(t\), start the physical middle word
at a symbol \(a\in\mathbb Z_n\).  Its first \(m-q\) symbols are

\[
 P_{t,q}(a)=a+\left\{0,z_{t+1},z_{t+1}+z_{t+2},\ldots,
       \sum_{j=1}^{m-q-1}z_{t+j}\right\}\pmod n.
\tag{5.1}
\]

The extra chip in \(\iota(R^tz)\) occupies its last gap, so it does not
enter (5.1).  The unit voltage in Theorem 2.1 makes the physical lift visit
all \(n\) translation phases \(a\).  Therefore one quotient occurrence of
the orbit of \(P_{t,q}(0)\) covers every physical member of that target
orbit.

For a lower translation orbit \(O\), put

\[
 a_{z,q}(O)=|\{t\in\mathbb Z_r:[P_{t,q}(0)]=O\}|.
\tag{5.2}
\]

Then

\[
                         \sum_Oa_{z,q}(O)=r.
\tag{5.3}
\]

At \(q=0\), the positive entries of (5.2) are exactly the middle form
vertices of the packet, each with multiplicity one.  Hence (4.4) is the
\(q=0\) system.

At positive depth, a packet selection \(x\) covers every lower target if
and only if

\[
 \boxed{
 \sum_z a_{z,q}(O)x_z\ge1
 \qquad(1\le q\le H,\ O\in\mathscr O_q).}
\tag{5.4}
\]

These inequalities must be imposed on the same variables as the middle
matching constraints.  There is no implication from (4.4) to (5.4).

When \(n\) is composite, a target \(Q\) of rank \(m-q\) may have
translation stabilizer order

\[
                         h(Q)\mid\gcd(n,m-q).
\tag{5.5}
\]

One quotient occurrence then covers every member of its orbit with
multiplicity \(h(Q)\); inequality (5.4) is still the correct cover
condition.  Nonfree targets are exponentially sparse for
\(q\le A\sqrt m\): a target stabilized by a subgroup of order \(d\ge3\)
is a union of subgroup orbits and there are at most
\(\binom{n/d}{(m-q)/d}\le2^{n/d}\) of them.  Thus

\[
 |\mathscr O_q|=(1+e^{-\Omega(m)}){1\over n}
                         \binom n{m-q}.
\tag{5.6}
\]

Since the total number of depth-\(q\) quotient occurrences in a perfect
middle packet factor is \(T\), its raw supply/demand ratio is

\[
 {T\over|\mathscr O_q|}
 =(1+o(1)){\binom nm\over\binom n{m-q}}
 =(1+o(1))\prod_{i=1}^q{m+1+i\over m-q+i}.
\tag{5.7}
\]

For \(q=A\sqrt m+O(1)\),

\[
 \log {\binom nm\over\binom n{m-q}}
 ={q^2+q\over m}+O(q^3/m^2)=A^2+o(1),
\tag{5.8}
\]

so (5.7) tends to \(e^{A^2}\).  The Gaussian prefix system therefore has
strict marginal slack, but not compatible-source slack.  In fact the
exact completion kernel for a target with gap word
\(g=(g_1,\ldots,g_{m-q})\) is

\[
                         D_q(g)=\sum_i\binom{g_i-2}{q}.
\tag{5.9}
\]

It vanishes unless some target gap is at least \(q+2\).  At
\(q=A\sqrt m\), the proportion of target forms satisfying that condition
is at most

\[
 (m-q){\binom{2m-q-1}{m-q-1}\over\binom{2m}{m-q-1}}
 =\exp\{-A(\log2)\sqrt m+O_A(\log m)\}=o(1).
\tag{5.10}
\]

Thus (5.4) is impossible for almost every Gaussian-depth target even if
all parent packets are available.  The missing-shadow obstruction is
compatibility, not total capacity or composite stabilizers.

## 6. Exact boundary

The proved component theorem is

\[
 \boxed{
 \begin{gathered}
 \text{all odd form classes admit one-chip packet options;}\\
 \text{every packet has unit voltage, even for composite }2m+1;\\
 \text{one phase gives }O(W/m^2)\text{ components on at least}
       \ (1/2-o(1))T\text{ forms.}
 \end{gathered}}
\tag{6.1}
\]

The exact remaining middle theorem is the near-perfect or perfect cyclic
deletion-code matching (4.4).  It is stronger than choosing a favorable
phase and weaker than constructing one global Ucycle.  It contains all bad
classes automatically.

After it, lower-prefix coverage is formally the augmented matching system
(5.4), but the consecutive-prefix version is refuted by (5.9)--(5.10).
A complete coefficient-one theorem would need a nonconsecutive or
re-atlased compiler before it could use the weaker target

\[
                         T-\sum_F\mathbf1_{\{F\ {\rm covered}\}}=o(T)
\tag{6.2}
\]

together with aggregate \(o(T)\) quotient prefix holes; their physical
lifts then leave \(o(W)\) masks.  A literal all-form Ucycle decomposition,
however, still requires an exact residual Euler absorber.

This is the sharp point reached by the circular-gap route: the awesome-form
omission and composite-voltage problem are solved, the middle cyclic
deletion-code near-matching remains open, and the original common
consecutive-prefix augmentation is false because of the Gaussian
large-gap cut.
