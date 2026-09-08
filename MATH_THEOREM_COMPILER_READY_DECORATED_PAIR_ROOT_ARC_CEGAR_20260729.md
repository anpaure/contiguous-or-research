# Compiler-ready decorated pairs: the exact twisted-omission and root/arc gate

Date: 2026-07-29

Status: proved an exact necessary-and-sufficient carrier-level theorem for
the existence of an equivariant one-core whose weighted quotient Hall graph
passes. A failed weighted min-cut now has an exact additive projection to a
small cyclic omission automaton. The forced-port test is proved to be only
an outer relaxation. No compiler-ready \(k=15\) carrier is constructed.

This strengthens
MATH_THEOREM_EQUIVARIANT_GRADED_COMPILER_QUOTIENT_HALL_20260729.md and
incorporates the corrections in
MATH_AUDIT_CLAUDE_RECENT_EQUIVARIANT_CONSTRUCTION_20260729.md and
THREAD_C15_WEIGHTED_ORBIT_QUOTIENT_HALL_AUDIT_20260729.md.

## 1. Scope and notation

Let \(G=C_k=\langle\rho\rangle\) act on coordinates
\(\mathbb Z_k\), let \(W=kN\), and suppose that a cyclic erosion row
\(P=(P_i)_{i\in\mathbb Z_W}\) has strict-spiral symmetry

\[
 P_{i+N}=\rho^vP_i,
 \qquad \gcd(v,k)=1.
\tag{1.1}
\]

All indices and the twisted closing seam in (1.1) are part of the
hypothesis. In the intended application \(P\) is the rank-\(h\) maximal
depth-\(d\) erosion of a resident Johnson carrier \(T\), with

\[
 k=15,\quad d=3,\quad h=5,\quad N=429.
\tag{1.2}
\]

The carrier shadow hypotheses and an upper-safe linear cut remain separate
conditions. This note characterizes exactly the missing lower
compiler-readiness condition

\[
 \exists\,C\le P:\quad DC=DP,\quad C\text{ equivariant},\quad
 \mathcal G_C\text{ satisfies physical Hall}.
\tag{1.3}
\]

By the weighted-orbit theorem, physical Hall in (1.3) is equivalent to
weighted quotient Hall because the action on occurrence-labelled right
positions is free. The eventual physical matching may break symmetry.

## 2. The twisted coordinate-trace graph

Write a physical position uniquely as

\[
 i=j+sN,\qquad 0\le j<N,\quad s\in\mathbb Z_k.
\tag{2.1}
\]

For a physical coordinate incidence \((i,x)\), define its quotient root

\[
 \pi(i,x)=(j,\rho^{-sv}x).
\tag{2.2}
\]

Define the twisted trace graph \(\mathcal R_v\) on
\(\mathbb Z_N\times\mathbb Z_k\) by the edges

\[
 (j,a)(j+1,a)\quad(0\le j<N-1)
\tag{2.3}
\]

and

\[
 (N-1,a)(0,\rho^{-v}a).
\tag{2.4}
\]

Traversing one quotient block changes the coordinate label by
\(\rho^{-v}\). Hence \(\mathcal R_v\) has \(\gcd(k,v)\) cycles, each of
length \(Nk/\gcd(k,v)\); for unit voltage it is one \(W\)-cycle.

A root \((j,a)\) is **supported** when \(a\in P_j\). A supported root is
**forced** when it is adjacent in \(\mathcal R_v\) to an unsupported root.
Equivalently, define the aligned predecessor and successor

\[
 P^-_j=
 \begin{cases}
 P_{j-1},&j>0,\\
 \rho^{-v}P_{N-1},&j=0,
 \end{cases}
\qquad
 P^+_j=
 \begin{cases}
 P_{j+1},&j<N-1,\\
 \rho^vP_0,&j=N-1,
 \end{cases}
\tag{2.5}
\]

and put

\[
 F_j=(P_j\setminus P^-_j)\cup(P_j\setminus P^+_j).
\tag{2.6}
\]

Then the forced roots in layer \(j\) are exactly
\(\{(j,a):a\in F_j\}\).

## 3. Exact one-core theorem

### Theorem 3.1 (equivariant cores are stable omission sets)

Equivariant one-cores \(C\le P\) satisfying \(DC=DP\) are in bijection
with sets \(Z\) of quotient roots satisfying:

1. every member of \(Z\) is supported;
2. \(Z\) contains no forced root; and
3. \(Z\) is a stable set in \(\mathcal R_v\).

Writing \(Z_j=\{a:(j,a)\in Z\}\), the bijection is

\[
 C_{j+sN}=\rho^{sv}(P_j\setminus Z_j).
\tag{3.1}
\]

#### Proof

Given an equivariant core, put \((j,a)\in Z\) exactly when
\(a\in P_j\setminus C_j\). An unsupported root cannot be an omission by
definition. If a supported root has an unsupported neighbour, the union
identity on that trace edge forces the supported endpoint into \(C\); hence
the root is not in \(Z\). If two adjacent supported roots were both in
\(Z\), their coordinate would be absent from both core endpoints while
present in \(DP\), contradicting \(DC=DP\). Thus \(Z\) is stable and
avoids the forced roots.

Conversely, define \(C\) by (3.1). On a trace edge there are three cases.
If neither endpoint is supported, both sides of \(DC=DP\) omit the
coordinate. If exactly one endpoint is supported, that endpoint is forced
and is not in \(Z\), so the core union contains the coordinate. If both are
supported, stability prevents both from being omitted. Thus every
coordinate agrees on every derivative edge, including the twisted seam.
Equivariance is built into (3.1). Therefore \(DC=DP\). \(\square\)

Equivalently, one may choose one omission state

\[
 Z_j\subseteq P_j\setminus F_j
\tag{3.2}
\]

per quotient layer, subject to

\[
 Z_j\cap Z_{j+1}=\varnothing\quad(0\le j<N-1),
\qquad
 Z_{N-1}\cap\rho^vZ_0=\varnothing.
\tag{3.3}
\]

This is a monotone \(2\)-SAT, vertex-cover, or finite-state-cycle system.
In particular, one-core existence alone is vacuous: \(Z=\varnothing\)
gives \(C=P\). The content is finding one state cycle whose containment
graph passes Hall.

### Proposition 3.2 (the forced-port mask)

The word \(F=(F_j)\) is the pointwise intersection of all equivariant
one-cores:

\[
 F_j=\bigcap_C C_j.
\tag{3.4}
\]

Moreover, \(F\) itself is a one-core if and only if every proper positive
component of every coordinate trace has length at most three and there is
no all-positive trace-cycle component.

#### Proof

Theorem 3.1 forces every support-run endpoint into every core. Any
nonendpoint supported root can be omitted alone; a singleton omission is
stable and avoids the forced roots. This proves (3.4).

On a proper positive run, \(F\) selects exactly the two endpoints (one
vertex when the run has length one). These endpoints cover every
support-support edge exactly for run lengths at most three. On an
all-positive trace cycle there are no forced roots, so \(F\) is empty and
covers no edge. The result follows coordinatewise. \(\square\)

Thus Claude's forced-port word is not generally a core. It is the union
relaxation obtained by allowing a different core for every candidate edge.

## 4. Root footprints and simultaneous containment

Let

\[
 \mathcal S_h=\{S\subseteq[k]:1\le |S|\le h\}
\tag{4.1}
\]

be the flexible physical target family. For a physical incidence
\(e=(S,i)\), with \(i=j+sN\), define its quotient omission footprint

\[
 K(e)=
 \{\pi(i,x):x\in P_i\setminus S\}.
\tag{4.2}
\]

### Lemma 4.1 (simultaneous pin criterion)

A family \(\mathcal A\) of physical target-position incidences is
simultaneously contained by one equivariant one-core if and only if:

1. \(S\subseteq P_i\) for every \((S,i)\in\mathcal A\);
2. \(K(\mathcal A)=\bigcup_{e\in\mathcal A}K(e)\) contains no forced root;
   and
3. \(K(\mathcal A)\) is stable in \(\mathcal R_v\).

#### Proof

If \(C_i\subseteq S\subseteq P_i\), every coordinate of
\(P_i\setminus S\) is omitted by \(C_i\). Hence each footprint is contained
in the legal omission set of \(C\), proving necessity.

Conversely, use \(Z=K(\mathcal A)\) in Theorem 3.1. For every
\((S,i)\in\mathcal A\), the resulting core omits all of
\(P_i\setminus S\), and therefore \(C_i\subseteq S\subseteq P_i\).
\(\square\)

There is no higher-order one-core obstruction: after unary forced-root
legality, all incompatibility is pairwise along the trace edges.

### Theorem 4.2 (exact compiler-ready decorated-pair theorem)

Under the symmetry and free-right-action hypotheses, the following are
equivalent.

1. There is an equivariant one-core \(C\le P\), \(DC=DP\), whose weighted
   quotient containment graph passes Hall.
2. There is an equivariant one-core whose physical containment graph has a
   matching saturating \(\mathcal S_h\).
3. There is an injection
   \[
   \mu:\mathcal S_h\longrightarrow\mathbb Z_W
   \tag{4.3}
   \]
   such that \(S\subseteq P_{\mu(S)}\) for every \(S\), and the total
   footprint
   \[
   \bigcup_{S\in\mathcal S_h}K(S,\mu(S))
   \tag{4.4}
   \]
   avoids the forced roots and is stable in \(\mathcal R_v\).

#### Proof

The weighted quotient-Hall theorem gives the equivalence of 1 and 2,
including short target orbits; no equivariant matching is required.

Given 2, take its physical matching as \(\mu\). Every footprint in (4.4)
lies in the omission set of \(C\), so Lemma 4.1 proves 3.

Given 3, Lemma 4.1 produces one equivariant core containing every assigned
target at its assigned position. The injection is then a saturating
physical matching in its containment graph, proving 2. \(\square\)

Theorem 4.2 is the exact missing decorated-pair statement. A decoration
screen, an edgewise-union matching, or a quotient flow not tied to one
omission state does not meet its hypotheses.

## 5. Exact small-state quotient formulation

Let \(O\) be a target orbit, choose a representative \(S_O\), and write
\(w(O)=|O|\). At quotient layer \(j\), its possible roots are

\[
 \mathscr R_j(O)=
 \{\rho^\delta S_O:\ 0\le\delta<w(O),\
                    \rho^\delta S_O\subseteq P_j\}.
\tag{5.1}
\]

These are all relative phases, including for a short orbit: \(w(O)\) is
the least \(\rho\)-period, and \(\gcd(v,k)=1\) implies
\(\gcd(v,w(O))=1\), so the physical right-orbit phases normalize through
all \(\delta=0,\ldots,w(O)-1\).

For a collection \(X\) of target orbits and an omission state
\(Z\subseteq P_j\setminus F_j\), define

\[
 g_j^X(Z)=
 {\bf1}\!\left[
 \exists\,O\in X,\ R\in\mathscr R_j(O):
                 P_j\setminus R\subseteq Z
 \right].
\tag{5.2}
\]

For the core \(C_j=P_j\setminus Z_j\), this indicator is exactly one when
the quotient right orbit \(j\) belongs to the neighborhood of \(X\).

### Theorem 5.1 (cyclic omission-automaton Hall theorem)

An equivariant compiler-ready one-core exists if and only if there are
states \(Z_j\) satisfying (3.2)--(3.3) and, for every quotient target shore
\(X\),

\[
 \boxed{\qquad
 \sum_{j=0}^{N-1}g_j^X(Z_j)
 \ \ge\
 b(X):=
 \left\lceil{\sum_{O\in X}w(O)\over k}\right\rceil .
 \qquad}
\tag{5.3}
\]

#### Proof

For fixed states, Theorem 3.1 gives an equivariant core. Equation (5.2)
identifies its quotient neighborhood exactly. Since every right orbit has
physical capacity \(k\), weighted quotient Hall is

\[
 \sum_{O\in X}w(O)\le
 k\sum_jg_j^X(Z_j).
\]

The right side is a multiple of \(k\), so this is equivalent to (5.3).
Apply the weighted quotient-Hall theorem and then Theorem 4.2. \(\square\)

At \(k=15,d=3\), maximal-erosion chronology gives

\[
 F_i=\{\beta_{i-4},\alpha_i\},
\tag{5.4}
\]

with a one-coordinate set when the two ports coincide. Since
\(|P_i|=5\), every layer has at most \(2^4=16\) omission states (and usually
\(2^3=8\)).

The target quotient has \(329\) full orbits of weight \(15\), one
rank-three orbit of weight \(5\), and one rank-five orbit of weight \(3\).
If \(f(X)\) is the number of full orbits in \(X\), then

\[
 b(X)=
 \begin{cases}
 f(X),&X\text{ contains neither exceptional orbit},\\
 f(X)+1,&X\text{ contains at least one exceptional orbit}.
 \end{cases}
\tag{5.5}
\]

Consequently the weighted decision test is equivalently the two ordinary
unit Hall tests obtained by adjoining, separately, each exceptional orbit
to the \(329\) full-orbit graph. Indeed, a shore of full orbits alone has
threshold \(f\); adjoining either or both exceptional orbits raises the
integer threshold to \(f+1\), and the neighborhood with both contains the
neighborhood obtained with either one. This is a decision equivalence, not
two simultaneous physical matchings.

## 6. Exact min-cut projection for quotient CEGAR

Introduce one-hot variables \(y_{j,Z}\) selecting a state
\(Z\subseteq P_j\setminus F_j\), together with transition-arc variables
enforcing (3.3). If weighted max flow for an incumbent state cycle returns
a deficient shore \(X\), then the exact Benders row is

\[
 \boxed{\qquad
 \sum_j\sum_Z g_j^X(Z)y_{j,Z}\ge b(X).
 \qquad}
\tag{6.1}
\]

This is not a no-good for only the incumbent: it removes exactly every core
state cycle whose neighborhood of the certified shore is too small.
Repeated min-cut separation is finite and is necessary and sufficient by
Theorem 5.1.

Each score in (6.1) is a root condition. Writing

\[
 \mathcal K_{X,j}=
 \{P_j\setminus R:R\in\mathscr R_j(O),\ O\in X\},
\tag{6.2}
\]

one has

\[
 g_j^X(Z)=
 \bigvee_{K\in\mathcal K_{X,j}}[K\subseteq Z].
\tag{6.3}
\]

Footprints containing another available footprint are dominated and may be
deleted. The inclusion-minimal footprints form an antichain in
\(2^{P_j}\), so at \(h=5\) at most
\(\binom52=10\) active root patterns remain in a layer.

For a carrier-variable master, a local collar of six middle states (five
directed arcs) determines \(P_j\), its two ports (5.4), and all scores
\(g_j^X\). Therefore (6.1) remains valid after replacing \(y_{j,Z}\) by a
combined carrier-collar/core-state literal. The collar literal must be
enforced: dropping it replaces actual chronology by an envelope-union
relaxation. A collar crossing the quotient seam is aligned using the same
\(\rho^{-v}\) predecessor and \(\rho^v\) successor convention as (2.5).

If \(N_0\) is the incumbent quotient neighborhood of \(X\), the valid
novelty form

\[
 \sum_{j\notin N_0}\sum_Z g_j^X(Z)y_{j,Z}
 \ge b(X)-|N_0|
\tag{6.4}
\]

asks for the required number of new right blocks while allowing every old
block to survive optimistically.

### 6.1 Carrier-only projections

The pointwise forced-port union indicator is

\[
 e_j^X(P)=
 {\bf1}\!\left[
 \exists\,O\in X,\ R\in\mathscr R_j(O):
 F_j\subseteq R\subseteq P_j
 \right].
\tag{6.5}
\]

Every core neighborhood is contained in this union graph, so every
compiler-ready carrier necessarily satisfies

\[
 \sum_je_j^X(P)\ge b(X)
\quad\text{for every }X.
\tag{6.6}
\]

Equation (6.6) is the precise valid scope of the old forced-port Hall
screen. It is local in the same six-state/five-arc collar and is a sound
carrier-only CEGAR cut when it fails. For \(N>1\), it is incidencewise
exact as the union over all one-core graphs: if
\(F_j\subseteq R\subseteq P_j\), the single-layer footprint
\(P_j\setminus R\) avoids forced roots and is stable, so Theorem 3.1
extends it to a core. For \(N=1\), same-layer twisted adjacencies can make
the screen a strict outer relaxation. The intended \(k=15\) instance has
\(N=429\). Passing the union screen is not sufficient in either case.

A strictly stronger all-core obstruction for one fixed shore is

\[
 \eta_X(P)=
 \max_{\substack{Z_0,\ldots,Z_{N-1}\\\text{satisfy }(3.2)-(3.3)}}
 \sum_jg_j^X(Z_j).
\tag{6.7}
\]

This is an exact max-plus cyclic dynamic program with at most sixteen states
per layer at \(k=15\). Therefore

\[
 \eta_X(P)<b(X)
\tag{6.8}
\]

proves that no equivariant one-core on that carrier can repair the shore
\(X\). Conversely, \(\eta_X(P)\ge b(X)\) proves only that this one shore
can be repaired by some core. The core may depend on \(X\).

## 7. Separations and counterexamples

### 7.1 The forced-port union can pass Hall with no common core

Take three cyclic positions and

\[
 P_0=\{x,a\},\qquad
 P_1=\{x,b\},\qquad
 P_2=\{x,c\}.
\tag{7.1}
\]

For the two-target subproblem \(\{\{a\},\{b\}\}\), the forced-port sets are

\[
 F_0=\{a\},\qquad F_1=\{b\},\qquad F_2=\{c\}.
\tag{7.2}
\]

Thus the edgewise-union graph has the matching

\[
 \{a\}\mapsto0,\qquad \{b\}\mapsto1.
\]

But these two incidences require omission of \(x\) at adjacent trace roots
0 and 1. Their footprints are not stable, so Lemma 4.1 proves that no
single one-core realizes the matching. Individual incidence feasibility
and Hall in the forced-port decoration screen are therefore strictly weaker
than compiler readiness.

### 7.2 Even every shore-specific optimum may use a different core

Take four cyclic positions

\[
 P_0=P_2=\{x,b\},\qquad
 P_1=P_3=\{x,a\},
\tag{7.3}
\]

and the target subproblem \(A=\{a\},B=\{b\}\). Target \(A\) is available
exactly when \(x\) is omitted at an odd position; target \(B\) is available
exactly when \(x\) is omitted at an even position.

For shore \(\{A\}\), the two odd omissions are compatible, so
\(\eta_{\{A\}}=2\). Similarly \(\eta_{\{B\}}=2\). For
\(\{A,B\}\), a maximum stable set of the four-cycle has size two, so
\(\eta_{\{A,B\}}=2\). Hence every shore separately satisfies its Hall
threshold.

Nevertheless no one core passes Hall for both singletons. Every odd
position is adjacent to both even positions in this four-cycle, so a stable
omission set cannot contain an odd and an even root. This proves the strict
quantifier separation

\[
 \forall X\ \exists C_X\text{ repairing }X
 \quad\not\Longrightarrow\quad
 \exists C\ \forall X\text{ Hall-valid}.
\tag{7.4}
\]

Thus the exact joint state rows (6.1), not merely the carrier-only values
\(\eta_X\), are required for sufficiency.

Both examples are abstract one-core systems, not counterexamples inside the
full strict \(k=15\) Johnson-carrier class.

### 7.3 Exact audit separation

On Claude's fresh passing \(k=11\) carrier, the forced-port checker reports
READY, but its forced mask \(F\) satisfies

\[
 DF\ne DP
\]

on \(330\) of \(462\) cyclic edges. This is an exact finite counterexample
to treating the forced-port mask as the compiler core. That carrier does
possess a different equivariant one-core and compiles optimally, so it is
not a counterexample to existence of some passing core.

Finally, \(C=P\) is always a one-core, but when \(h>1\) it gives every
singleton target degree zero. One-core existence without Hall is no
readiness statement at all.

## 8. Exact proved and conditional boundary

Proved here:

1. all equivariant one-cores are exactly the stable omission cycles of
   Theorem 3.1;
2. a compiler-ready decorated pair is exactly a conflict-free physical
   target injection, Theorem 4.2;
3. weighted quotient Hall over all cores is exactly the small-state system
   (5.3);
4. every failed min-cut gives the exact additive root/state row (6.1);
5. failure of (6.6) or (6.8) is a sound carrier-only obstruction; and
6. neither forced-port Hall nor separately optimized shore tests are
   sufficient for one common core.

Still unproved:

* existence of a resident, shadow-complete strict \(k=15\) carrier admitting
  a state cycle satisfying every row (5.3);
* a theorem that the local carrier decoration constraints force such a
  state cycle; and
* an upper-safe physical cut for any future passing \(k=15\) pair.

An aggregate quotient flow remains only a decision certificate. After a
state cycle passes, one must recover a phase-resolved physical matching
before emitting the word. The upper-safe cut is then checked separately.
