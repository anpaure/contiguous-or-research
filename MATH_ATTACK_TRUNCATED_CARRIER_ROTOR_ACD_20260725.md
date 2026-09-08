# Low-boundary automorphism descent for truncated carrier rotors

Date: 2026-07-25

Pure mathematics only.  No computation, search, solver, web input, or
probabilistic black box is used.

## 0. Verdict

The automorphism-overlay descent mechanism specializes exactly to the
truncated carrier-rotor family, but rotor branching does not by itself
supply the required \(\Theta(M)\) shallow movement.

At the calibrated crossing let

\[
M=m+H,\qquad
T=MN_H=W-o(W),\qquad
Q=o(H),\qquad Q=o(M).
\tag{0.1}
\]

Choose one length-\(M\) quotient rotor path in every \(M\)-carrier.  If its
middle-owner collision is \(C_0=o(W)\), then every coordinate permutation
\(g\) supplies a second valid path family whose owner occurrence vector
differs by only

\[
2(W-T+2C_0)=o(W).
\tag{0.2}
\]

Matching the common owner occurrences produces a carrier overlay.  A union
of weak components is a positive congestion-one switch; an arbitrary cut
\(A\) has the exact owner counterterm

\[
\sum_{U\xrightarrow{X}V}
\bigl(\mathbf1_A(V)-\mathbf1_A(U)\bigr)e_X
\tag{0.3}
\]

plus the baseline \(o(W)\) unmatched-stub vector.  Thus the interface toll
is controlled exactly by the matched owner boundary.

The new rotor audit is negative in the local sense.

* If two rotor paths have the same directed owner sequence, their interior
  lower and upper flags are forced by that sequence:
  \[
  L_q(t)=\bigcap_{i=0}^{q}X_{t+i},
  \qquad
  U_q(t)=\bigcup_{i=0}^{q}X_{t-i}.
  \tag{0.4}
  \]
  Only the final \(q\) lower occurrences and initial \(q\) upper
  occurrences can differ.  Their total variation is \(O(q)\) at depth
  \(q\), hence \(O(Q^2)=o(MQ)\) over the whole truncated band.
* More strongly, the hidden branch choice \(x_t\) becomes the forced owner
  departure exactly \(Q\) steps later:
  \[
  x_t=X_{t+Q}\setminus X_{t+Q+1}.
  \tag{0.5}
  \]
  A fixed owner sequence determines every quotient state except an
  \(O(Q)\)-state boundary collar.
* For two owner-preserving path decompositions, let \(D\) be the number of
  owner occurrences whose successor is rethreaded.  At depth \(q\), at
  most \(qD+O(qN_H)\) starts can change.  In particular,
  \(\Theta(M)\) movement per active carrier at depth one requires
  \(\Theta(M)\) changed owner-successor arcs per carrier.

Consequently the large state outdegree

\[
(m-Q)(H-Q)
\tag{0.6}
\]

does not prove automorphism component descent.  It provides many lifts and
many next states, but owner-fixed branching is only a boundary absorber.
Macroscopic descent requires a new **carrier rethreading theorem**: the same
owner occurrence set must admit two legal rotor path decompositions whose
successor factors differ on a linear fraction of their arcs and whose
component switch has positive global Gain minus Loss.

There is no proved obstruction to such a global rethreading.  There is also
no construction of it in the existing rotor notes.  Thus the exact answer
is:

\[
\boxed{\text{local rotor branching: no;}
\quad\text{global owner rethreading: open.}}
\tag{0.7}
\]

Complete long-run orientation cubes demonstrate that owner-identical linear
rethreading is possible at length \(2^{\Omega(Q)}\), but that is far above
the allowed carrier-path length \(M\).  The sharp raw-capacity subgate is a
sparse \(M-o(M)\)-vertex cube subset carrying two long-run Hamilton cycles
with linear edge symmetric difference, denoted \(\mathrm{SLR}_Q\) below.

## 1. Truncated carrier paths and their loads

For a carrier \(U\in\binom{[2m]}M\), a quotient state is

\[
\omega=(L;z_1,\ldots,z_{2Q};R_U),
\tag{1.1}
\]

where

\[
|L|=m-Q,\qquad |R_U|=H-Q,
\]

and the displayed parts partition \(U\).  A rotor edge chooses

\[
x\in L,\qquad y\in R_U
\]

and sends \(\omega\) to

\[
(L-x+y;x,z_1,\ldots,z_{2Q-1};R_U-y+z_{2Q}).
\tag{1.2}
\]

The middle owner and signed depth-\(q\) flags are

\[
X(\omega)=L+z_1+\cdots+z_Q,
\tag{1.3}
\]

\[
L_q(\omega)=L+z_1+\cdots+z_{Q-q},
\tag{1.4}
\]

\[
U_q(\omega)=L+z_1+\cdots+z_{Q+q}.
\tag{1.5}
\]

Let

\[
P_U=(\omega_{U,0},\ldots,\omega_{U,M-1})
\tag{1.6}
\]

be one directed walk of \(M\) state endpoints.  Walks are sufficient for
literal compilation.  When owner collision is being minimized, simple
owner paths are preferable but are not assumed in the identities below.

A path family

\[
\mathcal F=\{P_U:U\in\tbinom{[2m]}M\}
\tag{1.7}
\]

has exactly

\[
T=MN_H
\tag{1.8}
\]

state occurrences.  Let \(\mu_0(X)\) be its middle-owner load and set

\[
C_0(\mathcal F)=\sum_X(\mu_0(X)-1)_+.
\tag{1.9}
\]

The number of missing middle owners is exactly

\[
h_0=W-T+C_0(\mathcal F).
\tag{1.10}
\]

Thus \(C_0=o(W)\) is the precise owner near-transversal condition.

At a signed rank \(r=m\pm q\), let \(\mu_r(S)\) be the flag occurrence
load and put

\[
\mathcal E_r(\mathcal F)
=\sum_S(\mu_r(S)-1)_+.
\tag{1.11}
\]

The flag-hole identity is

\[
h_r=N_q-T+\mathcal E_r(\mathcal F),
\tag{1.12}
\]

or equivalently

\[
h_r-(N_q-T)_+
=\mathcal E_r(\mathcal F)-(T-N_q)_+.
\tag{1.13}
\]

The calibrated scalar floors in (1.13), summed over the full represented
band, are \(o(W)\).  Therefore the truncated path theorem is equivalent to
finding a path family with \(C_0=o(W)\) and aggregate excess collision
\(o(W)\) through \(q\le Q\).

## 2. Exact automorphism-overlay reduction

Let \(g\in S_{2m}\).  Coordinate permutation commutes with the rotor
recurrence (1.2).  Define

\[
P_U^g=gP_{g^{-1}U},
\qquad
\mathcal F^g=\{P_U^g\}.
\tag{2.1}
\]

This is again one valid length-\(M\) rotor walk in every carrier.  At every
rank,

\[
\mu_r(\mathcal F^g)=g\mu_r(\mathcal F).
\tag{2.2}
\]

### Theorem 2.1 (owner-near-preserving frame change)

For every path family \(\mathcal F\) and coordinate permutation \(g\),

\[
\boxed{
\|g\mu_0-\mu_0\|_1
\le2(W-T+2C_0(\mathcal F)).
}
\tag{2.3}
\]

Hence a middle near-transversal and its coordinate image differ by only
\(o(W)\) owner occurrences.

#### Proof

Let \(\mathbf1\) be the all-ones owner vector.  By (1.10),

\[
\|\mu_0-\mathbf1\|_1
=h_0+C_0
=W-T+2C_0.
\tag{2.4}
\]

Coordinate permutation fixes \(\mathbf1\) and preserves \(\ell^1\).
The triangle inequality gives (2.3).  \(\square\)

Match the maximum possible number of old and new occurrences of every
owner.  A matched occurrence of owner \(X\), old in carrier \(U\) and new
in carrier \(V\), gives a directed overlay edge

\[
U\xrightarrow{\,X\,}V.
\tag{2.5}
\]

The total number of unmatched old and new stubs is
\(\|g\mu_0-\mu_0\|_1=o(W)\).

For a carrier set \(A\), use \(P_U^g\) at \(U\in A\) and \(P_U\) outside
\(A\).  Call the hybrid \(\mathcal F_A\).

### Theorem 2.2 (exact owner interface formula)

There is a vector \(u_A\), supported on unmatched owner stubs, such that

\[
\boxed{
\mu_0(\mathcal F_A)-\mu_0(\mathcal F)
=\sum_{U\xrightarrow{X}V}
\bigl(\mathbf1_A(V)-\mathbf1_A(U)\bigr)e_X+u_A,
}
\tag{2.6}
\]

with

\[
\|u_A\|_1\le2(W-T+2C_0(\mathcal F)).
\tag{2.7}
\]

Consequently

\[
\|\mu_0(\mathcal F_A)-\mu_0(\mathcal F)\|_1
\le|\partial_GA|+2(W-T+2C_0),
\tag{2.8}
\]

where \(\partial_GA\) is the multiset of matched overlay edges crossing the
cut.

If \(A\) is a union of weak overlay components, then

\[
|\partial_GA|=0,
\tag{2.9}
\]

so the switch has congestion one and preserves the middle near-transversal
up to the unavoidable baseline \(o(W)\).

#### Proof

Every matched internal occurrence is used on both sides of the hybrid and
cancels.  A matched edge crossing the cut contributes with the sign in
(2.6).  All remaining terms are unmatched stubs.  This proves (2.6)--(2.8).
Equation (2.9) is the definition of weak component closure.  \(\square\)

This theorem is occurrence-exact and remains valid when individual paths
self-collide.

## 3. Exact flag descent on a carrier component

Let \(\mathcal F,\mathcal G\) be two path families.  For a carrier set
\(A\), write \(\mathcal F_A\) for the family obtained by replacing the old
paths on \(A\) by the comparison paths.

For a signed target \(S\), let

\[
a_S=\text{number of old hits outside }A,
\]

\[
u_S=\text{number of old hits inside }A,
\qquad
v_S=\text{number of comparison hits inside }A.
\tag{3.1}
\]

Define

\[
\operatorname{Gain}_A
=\#\{S:a_S=0,\ u_S=0,\ v_S>0\},
\tag{3.2}
\]

\[
\operatorname{Loss}_A
=\#\{S:a_S=0,\ u_S>0,\ v_S=0\},
\tag{3.3}
\]

where \(S\) ranges over all controlled lower and upper targets.

### Lemma 3.1 (exact Gain-Loss derivative)

\[
\boxed{
\operatorname{Hol}(\mathcal F_A)-\operatorname{Hol}(\mathcal F)
=\operatorname{Loss}_A-\operatorname{Gain}_A.
}
\tag{3.4}
\]

#### Proof

If \(a_S>0\), the target remains covered.  If \(a_S=0\), its hole
indicator increases exactly when \(u_S>0,v_S=0\), and decreases exactly
when \(u_S=0,v_S>0\).  Sum these indicator changes.  \(\square\)

No owner argument enters (3.4).  The owner overlay is what makes the
positive flag switch affordable.

### Rotor automorphism component descent \(\mathrm{RACD}_Q\)

There is a finite admissible class of one-path-per-carrier families, closed
under the following switches, and a sequence \(\varepsilon_m\downarrow0\)
such that whenever

\[
C_0(\mathcal F)=o(W),
\qquad
\operatorname{Hol}_{\le Q}(\mathcal F)>\varepsilon_mW,
\tag{3.5}
\]

there are a coordinate permutation \(g\) and a carrier set \(A\) for which

\[
|\partial_GA|=o(W),
\tag{3.6}
\]

\[
\mathcal F_A\text{ remains in the admissible owner-near-transversal class},
\tag{3.7}
\]

and

\[
\boxed{
\operatorname{Gain}_A(\mathcal F,\mathcal F^g)
>
\operatorname{Loss}_A(\mathcal F,\mathcal F^g).
}
\tag{3.8}
\]

Finite descent using (3.4) would prove the truncated path theorem, provided
the admissible class has a uniform \(o(W)\) owner-collision bound.  The path
compilation cost remains \(W+o(W)\) because every switch retains one
length-\(M\) path per carrier.

The rest of this note audits whether local rotor branching proves (3.8).

## 4. The delayed owner law

Write one path as

\[
\omega_0,\omega_1,\ldots,\omega_{s-1},
\tag{4.1}
\]

and let \(x_t,y_t\) be the choices on the edge
\(\omega_t\to\omega_{t+1}\).  Write \(z_{t,i}\) for queue coordinate \(i\)
at time \(t\), and \(X_t=X(\omega_t)\).

The queue recurrence gives

\[
z_{t+1,1}=x_t,
\qquad
z_{t+1,i}=z_{t,i-1}\quad(2\le i\le2Q).
\tag{4.2}
\]

Hence

\[
z_{t,i}=x_{t-i}
\qquad(t\ge i).
\tag{4.3}
\]

The owner transition is

\[
X_{t+1}=X_t-z_{t,Q}+y_t.
\tag{4.4}
\]

Put

\[
a_t=X_t\setminus X_{t+1},
\qquad
b_t=X_{t+1}\setminus X_t.
\tag{4.5}
\]

Then

\[
a_t=z_{t,Q},
\qquad
b_t=y_t.
\tag{4.6}
\]

Combining (4.3) and (4.6) proves the exact delay identity.

### Lemma 4.1 (branch choices become forced departures)

For every \(0\le t\le s-Q-2\),

\[
\boxed{
x_t=a_{t+Q}
=X_{t+Q}\setminus X_{t+Q+1}.
}
\tag{4.7}
\]

Thus all core choices except those on the final \(Q\) edges are determined
by the directed owner sequence.

There is a dual residence constraint.  A coordinate \(a_t\) which leaves
the owner at edge \(t\) enters queue position \(Q+1\), reaches position
\(2Q\), and only then enters \(R_U\).  It cannot return to the owner before
edge \(t+Q+1\).  Likewise \(b_t\), newly inserted into the owner, cannot
leave it before edge \(t+Q+1\).  Every coordinate run in or out of the
owner therefore has length at least \(Q+1\).

### Lemma 4.2 (interior state reconstruction)

For

\[
2Q\le t\le s-Q-1,
\tag{4.8}
\]

the entire quotient state \(\omega_t\) is determined by the carrier \(U\)
and the directed owner sequence.  Explicitly,

\[
z_{t,i}=a_{t-i+Q}
\qquad(1\le i\le2Q),
\tag{4.9}
\]

\[
L_t=X_t\setminus\{z_{t,1},\ldots,z_{t,Q}\},
\tag{4.10}
\]

\[
R_{U,t}
=U\setminus
\left(
L_t\cup\{z_{t,1},\ldots,z_{t,2Q}\}
\right).
\tag{4.11}
\]

#### Proof

For (4.9), use \(z_{t,i}=x_{t-i}\) and then (4.7).  The inequalities in
(4.8) ensure that every displayed index exists.  Equations
(4.10)--(4.11) follow from the owner definition and the state partition.
\(\square\)

Thus the apparent hidden choice at time \(t\) is not permanent entropy.  It
is a \(Q\)-step look-ahead choice encoded later in the owner chronology.

## 5. Flags are owner-path statistics

The delay law gives an even sharper conclusion at the flag level.

### Theorem 5.1 (exact path formulas)

For \(0\le q\le Q\),

\[
\boxed{
L_q(\omega_t)=\bigcap_{i=0}^{q}X_{t+i}
}
\qquad(t+q<s),
\tag{5.1}
\]

\[
\boxed{
U_q(\omega_t)=\bigcup_{i=0}^{q}X_{t-i}
}
\qquad(t\ge q).
\tag{5.2}
\]

#### Proof

During the next \(q\) transitions, the owner loses in order

\[
z_{t,Q},z_{t,Q-1},\ldots,z_{t,Q-q+1}.
\]

No inserted coordinate can leave within \(q\le Q\) steps.  Therefore the
intersection of the \(q+1\) owners is

\[
X_t-\{z_{t,Q-q+1},\ldots,z_{t,Q}\}
=L_t+z_{t,1}+\cdots+z_{t,Q-q},
\]

which is (5.1).  The reverse argument says that the coordinates present in
the preceding owners but absent from \(X_t\) are

\[
z_{t,Q+1},\ldots,z_{t,Q+q}.
\]

Their union with \(X_t\) is (5.2).  \(\square\)

### Corollary 5.2 (owner-fixed branching is boundary-only)

Let \(P,P'\) be two rotor paths with the same directed owner sequence.
Then at lower depth \(q\) all flags agree except possibly the final \(q\)
state occurrences, and at upper depth \(q\) all flags agree except possibly
the initial \(q\) occurrences.  Hence

\[
\|B_{m-q}P-B_{m-q}P'\|_1\le2q,
\tag{5.3}
\]

\[
\|B_{m+q}P-B_{m+q}P'\|_1\le2q.
\tag{5.4}
\]

Summing over the truncated band,

\[
\sum_{q=1}^{Q}
\left(
\|B_{m-q}(P-P')\|_1+
\|B_{m+q}(P-P')\|_1
\right)
\le2Q(Q+1)=O(Q^2).
\tag{5.5}
\]

Since \(Q=o(M)\), this is \(o(MQ)\).  In particular, hidden state branching
over a fixed owner path cannot supply \(\Theta(M)\) movement at any fixed
shallow rank.

This conclusion is substantially stronger than merely observing that the
last \(Q\) choices \(x_t\) are free.  It says all certified non-boundary
flags are functions of the owner chronology alone.

## 6. Rethreading the owner occurrences

An exact owner-preserving component may use different owner orders.  This
is the only remaining way branching can have macroscopic shadow effect.

Consider two decompositions of the same labelled owner occurrences into
\(k\) directed rotor paths.  Match equal owner occurrences between the two
sides.  Each side defines a partial successor map, undefined at its \(k\)
path endpoints.

Let \(D\) be the number of matched nonendpoint owner occurrences at which
the old and new successors differ.  The \(2k\) old and new path endpoints
are counted separately.

### Theorem 6.1 (successor-rethreading locality)

At lower depth \(q\), a start can change only if its next \(q\) owner arcs
contain a rethreaded successor or meet a path endpoint.  The number of
changed starts is at most

\[
q(D+2k).
\tag{6.1}
\]

The same bound holds at upper depth \(q\).  Consequently

\[
\|B_{m-q}(\mathcal G-\mathcal F)\|_1
\le2q(D+2k),
\tag{6.2}
\]

\[
\|B_{m+q}(\mathcal G-\mathcal F)\|_1
\le2q(D+2k).
\tag{6.3}
\]

#### Proof

By Theorem 5.1, a lower flag is the intersection along a directed
\(q\)-edge owner path.  If all those successors agree and no endpoint is
met, the two paths and their intersection agree.  Each exceptional
successor lies in at most \(q\) possible forward windows.  There are at
most \(2k\) old and new endpoint exceptions.  This proves (6.1), and each
changed start contributes at most one deletion and one insertion, proving
(6.2).  Reverse the paths and use the union formula for (6.3).
\(\square\)

At depth one the sharper bound is

\[
\|B_{m-1}(\mathcal G-\mathcal F)\|_1+
\|B_{m+1}(\mathcal G-\mathcal F)\|_1
\le4(D+2k).
\tag{6.4}
\]

### Corollary 6.2 (linear movement requires linear rethreading)

Suppose a component contains \(k\) active carriers and has
\(\Theta(kM)\) useful variation at depth one.  Then

\[
\boxed{D=\Theta(kM).}
\tag{6.5}
\]

More generally, \(\Theta(kM)\) variation at a fixed depth \(q\) requires

\[
D=\Omega(kM/q)-O(k).
\tag{6.6}
\]

Thus a bounded number of local forks, diamonds, or queue-choice changes
cannot produce the desired component direction.  Almost every owner
successor must be globally rethreaded at the first shallow depth.

Summing (6.2)--(6.3) gives the raw band bound

\[
\sum_{q=1}^{Q}
\left(
\|B_{m-q}(\mathcal G-\mathcal F)\|_1+
\|B_{m+q}(\mathcal G-\mathcal F)\|_1
\right)
\le2Q(Q+1)(D+2k).
\tag{6.7}
\]

This upper bound is not a descent theorem: the changed occurrences may hit
already covered targets or destroy unique hits.  Gain-Loss remains the
necessary sign test.

### Theorem 6.3 (exact cyclic owner-lift criterion)

Let

\[
X_0,X_1,\ldots,X_{s-1}
\tag{6.8}
\]

be a directed cyclic Johnson walk of \(m\)-sets inside one carrier \(U\),
with

\[
X_{t+1}=X_t-a_t+b_t
\tag{6.9}
\]

for cyclic indices.  Assume \(s>2Q\).

This owner cycle is the middle projection of a cyclic quotient
carrier-rotor trajectory if and only if every coordinate has every finite
residence run in the owners, and every finite nonresidence run, of length at
least \(Q+1\).

When the condition holds, the quotient lift is forced:

\[
\boxed{
z_{t,i}=a_{t+Q-i}
\qquad(1\le i\le2Q),
}
\tag{6.10}
\]

\[
L_t=X_t\setminus\{a_t,a_{t+1},\ldots,a_{t+Q-1}\},
\tag{6.11}
\]

\[
R_{U,t}
=(U\setminus X_t)
\setminus\{a_{t-1},a_{t-2},\ldots,a_{t-Q}\}.
\tag{6.12}
\]

The rotor choices are

\[
x_t=a_{t+Q},
\qquad
y_t=b_t.
\tag{6.13}
\]

#### Proof

Necessity is the residence conclusion of Lemma 4.1, applied cyclically.

For sufficiency, the residence hypothesis says that the \(Q+1\) future
departures

\[
a_t,a_{t+1},\ldots,a_{t+Q}
\]

are distinct members of \(X_t\), while the \(Q\) preceding departures

\[
a_{t-1},\ldots,a_{t-Q}
\]

are distinct members of \(U\setminus X_t\).  It also says that the arriving
coordinate \(b_t\) is not among those preceding departures.  Therefore
(6.10)--(6.12) have the required block sizes,
\(x_t\in L_t\), and \(y_t\in R_{U,t}\).

Substitution gives

\[
L_t-x_t+y_t
=X_{t+1}\setminus
\{a_{t+1},\ldots,a_{t+Q}\}
=L_{t+1}.
\]

The queue in (6.10) shifts by one after inserting \(a_{t+Q}\), and
(6.12) satisfies the corresponding tail recurrence after deleting \(b_t\)
and receiving \(a_{t-Q}\).  Hence (1.2) holds at every cyclic step.

Finally, (6.10)--(6.12) show uniqueness of the quotient state over the
owner cycle.  \(\square\)

### Corollary 6.4 (rethreading is a long-residence factor problem)

For cyclic factors, two-factor rotor rethreading is equivalent to finding
two decompositions of the same owner occurrences into directed Johnson
cycles such that:

1. both successor factors have coordinate residence and nonresidence at
   least \(Q+1\); and
2. their successor maps differ on \(\Theta(kM)\) occurrences.

Once such owner factors exist, their rotor lifts are automatic and unique.
Conversely every cyclic rotor rethreading projects to such a pair.

For linear paths, it is enough to construct these cyclic factors and cut
one edge per carrier.  The resulting \(O(QN_H)=o(W)\) endpoint collar is
already allowed by the word ledger.

Thus the core open problem is not state-graph branching.  It is a
long-residence Johnson two-factor exchange on fixed owners.

## 7. Parked carrier coordinates: low boundary with zero gain

The truncated rotor does supply very long overlaps between neighboring
carriers.  This is useful for diagnosing the exact missing ingredient.

Let \(U,V\) be carriers at top-layer Johnson distance

\[
d=|U\setminus V|=|V\setminus U|,
\tag{7.1}
\]

and put \(K=U\cap V\).  Assume

\[
H-Q-d\ge2.
\tag{7.2}
\]

Choose a common prefix partition of \(K\):

\[
K=L\sqcup\{z_1,\ldots,z_{2Q}\}\sqcup R_K,
\tag{7.3}
\]

where

\[
|L|=m-Q,\qquad |R_K|=H-Q-d.
\]

Extend it to quotient states in the two carriers by

\[
R_U=R_K\sqcup(U\setminus V),
\qquad
R_V=R_K\sqcup(V\setminus U).
\tag{7.4}
\]

Restrict every rotor move to

\[
x\in L,\qquad y\in R_K.
\tag{7.5}
\]

The private carrier coordinates remain parked forever, and the displayed
prefix evolves identically in \(U\) and \(V\).

### Proposition 7.1 (long common rotor subgraph)

The restricted common rotor has outdegree

\[
(m-Q)(H-Q-d).
\tag{7.6}
\]

Every one of its walks lifts simultaneously to \(U\) and \(V\), with
identical owner and flag sequences at all controlled depths.

If the quantity in (7.6) is at least \(M\), it contains a simple directed
path of \(M\) state endpoints.

#### Proof

Under (7.5), recurrence (1.2) changes only the common parts
\(L,z_1,\ldots,z_{2Q},R_K\).  The private sets in (7.4) are never selected
and never enter the queue.  Hence the two lifted prefixes, owners, and flags
are identical.

Different pairs \((x,y)\) give different successors, proving (7.6).  Before
\(M\) vertices have been visited, every current state has at least \(M\)
distinct successors and fewer than \(M\) forbidden visited states, so one
successor is new.  Greedy continuation proves the last assertion.
\(\square\)

For a transposition \(g\) exchanging the private coordinates of adjacent
carriers and fixing \(K\), Proposition 7.1 can create a two-carrier overlay
component with \(M\) matched owner occurrences in each direction.  Its
owner boundary is zero.

But if the two common paths are merely exchanged between the two carriers,
their aggregate flag incidence is also merely exchanged:

\[
B_rP+B_rP'
\longmapsto
B_rP'+B_rP.
\tag{7.7}
\]

The component discrepancy is identically zero at every rank.

Thus rotor branching supplies the low-boundary half of \(\mathrm{RACD}_Q\)
in abundance, but not the descent half.  Parking private coordinates
maximizes owner overlap precisely by making the certified flags blind to
the carrier change.

## 8. The exact remaining carrier-rethreading gate

Theorems 5.1 and 6.1 isolate the missing construction.

> **Carrier rotor rethreading \(\mathrm{CRR}_Q\).**  Construct two
> one-path-per-carrier families on a common active carrier set such that:
>
> 1. their owner occurrence multisets agree exactly, or differ by \(o(W)\)
>    with an explicit low-boundary overlay;
> 2. their matched owner successor factors differ on
>    \(\Theta(M)\) arcs per active carrier;
> 3. each side is a legal collection of length-\(M\), radius-\(Q\)
>    quotient rotor paths;
> 4. the component flag vectors have \(\Theta(M)\) useful movement per
>    active carrier at the required shallow ranks; and
> 5. relative to the current global loads, at least one component satisfies
>    \[
>    \operatorname{Gain}>\operatorname{Loss}.
>    \tag{8.1}
>    \]

Conditions 1--3 are a positive path-factor reassembly problem.  Condition
4 is the throughput condition.  Condition 5 is the actual collision-descent
direction.

Strong connectivity of the quotient rotor proves only that one state can
reach another.  Large outdegree proves only that many simple paths exist.
Neither statement fixes the owner occurrence multiset while changing
\(\Theta(M)\) successor arcs.  Therefore neither proves
\(\mathrm{CRR}_Q\).

The smallest purely combinatorial subgate drops the global Gain-Loss test.

> **Two-factor rotor rethreading \(\mathrm{TFR}_Q\).**  Find a set
> \(\mathcal O\) of \(kM-o(kM)\) distinct middle owners, contained in a
> controlled family of \(k\) carriers, which has two legal decompositions
> into \(k\) length-\(M\) carrier-rotor paths whose successor maps differ on
> \(\Theta(kM)\) owner occurrences.

By Corollary 6.4, the clean cyclic version asks for two long-residence
Johnson cycle factors on the same owner set with linear successor symmetric
difference.  This formulation eliminates the quotient-state variables
entirely.

A proof of \(\mathrm{TFR}_Q\) would establish that rotor branching has the
necessary raw depth-one capacity.  It would not yet establish positive
descent, because the new intersection and union flags might be globally
misdirected.  Conversely, failure of \(\mathrm{TFR}_Q\) would sharply
refute the truncated-rotor ACD route.

### 8.1 Why the existing orientation-cube cycles do not prove
\(\mathrm{TFR}_Q\)

An orientation cube on \(s\) active coordinate pairs contains

\[
2^s
\tag{8.2}
\]

middle owners.  A Gray cycle with coordinate residence exceeding \(Q\)
has no repeated transition direction in any \(Q+1\) consecutive edges.
It therefore needs

\[
s\ge Q+1.
\tag{8.3}
\]

Consequently every complete orientation-cube packet with the required
radius-\(Q\) residence has size at least

\[
2^{Q+1}\gg M.
\tag{8.4}
\]

The complete cube really does have the required raw rethreading.  Let \(C\)
be one long-run Hamilton cycle, let \(n_i\) be its number of direction-\(i\)
edges, and put \(L=2^s\).  The direction-gap condition gives

\[
n_i\le\frac{L}{Q+1},
\qquad
\sum_i n_i=L.
\tag{8.4a}
\]

Average the edge overlap of \(C\) with its translations \(C+v\) over all
\(v\in\{0,1\}^s\).  Two cube edges can be translations of one another only
when they have the same direction, and the two endpoint alignments give

\[
\frac1{2^s}\sum_v|E(C)\cap E(C+v)|
=2^{1-s}\sum_i n_i^2
\le\frac{2L}{Q+1}.
\tag{8.4b}
\]

Hence some translation satisfies

\[
|E(C)\triangle E(C+v)|
\ge2L-\frac{4L}{Q+1}
=\Theta(L).
\tag{8.4c}
\]

Translation preserves the owner set of the complete cube and preserves the
direction word.  Thus \(C,C+v\) are two owner-identical long-residence
factors with linear successor difference.

This valid owner-preserving rethreading occurs at packet length \(2^s\).
It does not fit the truncated carrier atom, which permits only \(M\) state
occurrences at one carrier.

Taking an \(M\)-vertex segment from each Gray cycle restores the length
ledger but destroys equality of the two owner sets.  No existing note
supplies a correlated choice of segments whose owner boundaries aggregate
to \(o(W)\).  Thus complete-cube branching proves neither
\(\mathrm{TFR}_Q\) nor \(\mathrm{RACD}_Q\).

The required new object is a sparse \(M\)-owner subgraph, inside a carrier
Johnson graph, supporting two linearly different Hamilton path factors
with two-sided residence \(Q+1\).  It cannot be obtained merely by taking a
full long-run orientation cube at the present scale.

### 8.2 A sharp sparse-cube subgate

The preceding object can be made completely explicit.

Fix \(s\le H\), a core \(K\) of size \(m-s\), disjoint coordinate pairs

\[
\{a_1,b_1\},\ldots,\{a_s,b_s\},
\tag{8.5}
\]

and a parked set \(P\) of size \(H-s\).  They form one carrier

\[
U=K\sqcup P\sqcup\bigsqcup_{i=1}^s\{a_i,b_i\}.
\tag{8.6}
\]

For \(\epsilon\in\{0,1\}^s\), let

\[
X(\epsilon)
=K\cup
\{a_i:\epsilon_i=0\}
\cup
\{b_i:\epsilon_i=1\}.
\tag{8.7}
\]

Hypercube edges become Johnson edges between the owners (8.7).

> **Sparse long-run two-cycle lemma \(\mathrm{SLR}_Q\).**  For some
> \(s\le H\), there is a set
> \[
> \mathcal V\subseteq\{0,1\}^s,
> \qquad
> |\mathcal V|=L=M-o(M),
> \tag{8.8}
> \]
> supporting two Hamilton cycles \(C,C'\) such that:
>
> 1. in each cycle, two uses of the same cube direction are separated by
>    at least \(Q+1\) edges; and
> 2. their undirected edge symmetric difference satisfies
>    \[
>    |E(C)\triangle E(C')|=\Theta(L).
>    \tag{8.9}
>    \]

### Proposition 8.1 (\(\mathrm{SLR}_Q\) gives raw rotor rethreading)

If \(\mathrm{SLR}_Q\) holds, the owner set

\[
\{X(\epsilon):\epsilon\in\mathcal V\}
\tag{8.10}
\]

has two cyclic radius-\(Q\) carrier-rotor decompositions whose successor
maps differ on \(\Theta(L)\) owners.

At both depth-one signs, their incidence-vector distance is exactly

\[
|E(C)\triangle E(C')|=\Theta(L).
\tag{8.11}
\]

#### Proof

The direction-gap condition says that, along either cycle, each selected
coordinate \(a_i\) or \(b_i\) remains in or out of the owner for at least
\(Q+1\) states.  Core coordinates are always present and parked coordinates
always absent.  Theorem 6.3 therefore lifts both cycles uniquely to quotient
rotor cycles on \(U\).

For a cube edge in direction \(i\), its lower depth-one color is

\[
K\cup\{\text{the fixed choice in every pair }j\ne i\},
\tag{8.12}
\]

and its upper color is (8.12) together with \(\{a_i,b_i\}\).  Either color
recovers the direction \(i\) and every outside orientation.  Hence distinct
undirected cube edges have distinct lower colors and distinct upper colors.
The depth-one incidence symmetric difference is therefore exactly the edge
symmetric difference, proving (8.11).  \(\square\)

The lemma is calibrated to the path ledger: deleting one edge from each
cycle gives two linear rotor paths, while \(M-L=o(M)\) residual owners per
active carrier cost \(o(W)\) in aggregate when the deficit is
\(o(M)\).

\(\mathrm{SLR}_Q\) is not proved here.  It is strictly smaller than
\(\mathrm{TFR}_Q\), and it cleanly separates raw rotor capacity from
global Gain-Loss.  The full-cube construction satisfies the two-cycle
requirements at size \(2^s\); the unsolved point is a sparse
\(M\)-vertex carrier-scale subset.

## 9. Consequences for the constant-one program

The truncated carrier theorem remains a valid sufficient target.  The
present audit changes how its dynamic freedom may be used.

1. The owner near-transversal must still be constructed first.
2. Coordinate-frame automorphisms then give comparison path families with
   only \(o(W)\) total owner discrepancy.
3. Low-boundary carrier cuts preserve that owner ledger.
4. Local changes of the hidden rotor choices can repair only
   \(O(Q^2)\) aggregate boundary flags per path.
5. Macroscopic collision descent requires global rethreading of the owner
   path factor, on a linear number of successor arcs.

Since \(N_H=(1+o(1))W/M\), an \(O(Q^2)\) branch absorber at every carrier
has total raw band capacity

\[
O(Q^2N_H)=O(WQ^2/M).
\tag{9.1}
\]

For the prescribed

\[
Q^2\asymp m\log\log m,
\]

this bound is \(O(W\log\log m)\) across all \(2Q\) rows, but only

\[
O(QN_H)=O(WQ/M)=o(W)
\tag{9.2}
\]

at a fixed typical boundary scale.  More decisively, at depth one its
capacity is only

\[
O(N_H)=O(W/M)=o(W).
\tag{9.3}
\]

Thus local branching cannot remove a macroscopic first-shadow collision
defect, regardless of its larger aggregate count over the growing band.

## 10. Audit ledger

### Proved

1. Coordinate automorphisms preserve the truncated rotor path class.
2. Any owner near-transversal and its coordinate image differ in only
   \(o(W)\) owner occurrences.
3. Formula (2.6) is the exact owner counterterm for an automorphism-overlay
   cut; weak components have zero matched boundary.
4. The exact flag-hole change of a carrier switch is Loss minus Gain.
5. Rotor core choices become forced owner departures after exactly \(Q\)
   steps.
6. A fixed directed owner sequence reconstructs every interior quotient
   state.
7. Every certified lower and upper flag away from the path endpoints is an
   intersection or union of a consecutive owner path.
8. Two rotor lifts of the same owner sequence differ in only \(O(q)\)
   occurrences at depth \(q\), and \(O(Q^2)\) over the whole band.
9. An owner-preserving component with \(\Theta(M)\) depth-one movement per
   carrier must rethread \(\Theta(M)\) owner-successor arcs per carrier.
10. A cyclic owner factor has a rotor lift exactly under the two-sided
    residence-\((Q+1)\) condition, and that lift is unique.
11. Rotor rethreading is therefore exactly a long-residence Johnson
    two-factor problem on fixed owners.
12. Neighboring carriers contain long common restricted rotors with zero
    owner boundary.
13. Exchanging such parked common paths has exactly zero aggregate shallow
    discrepancy.
14. Strong connectivity and large branching do not imply owner-multiset
    rethreading.
15. Full orientation-cube rethreadings have size at least
    \(2^{Q+1}\gg M\); truncating them loses automatic owner preservation.
16. The sparse long-run two-cycle lemma \(\mathrm{SLR}_Q\) would imply
    raw two-factor rotor rethreading with exactly linear depth-one shadow
    movement.

### Open

1. The initial owner near-transversal of length-\(M\) rotor paths.
2. Two-factor rotor rethreading \(\mathrm{TFR}_Q\).
3. The smaller sparse-cube subgate \(\mathrm{SLR}_Q\).
4. Directional shallow movement and the Gain-Loss inequality for those
   rethreadings.
5. Rotor automorphism component descent \(\mathrm{RACD}_Q\).
6. The truncated path theorem and coefficient one.

Rotor-path branching is therefore useful as an endpoint absorber and as a
source of many comparison paths.  It has not yet been converted into the
owner-preserving long component demanded by automorphism descent.  The live
mathematical object is no longer an arbitrary rotor path; it is two legal
rotor path factors on essentially the same owners with linearly different
successor structure.
