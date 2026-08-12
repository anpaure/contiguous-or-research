# K17 drop-12 H-source triple aperture-join factorization

**Date:** 2026-08-03  
**Status:** unconditional exact occurrence-domain theorem on the canonical
drop-12 parent. It factors every endpoint-disjoint triple containing one of
the 468 authenticated unary-empty H sources into fixed-arity provider
relations. It does not enumerate the domain, replay suppliers, or produce a
K17 word.

Canonical compressed/final SHA-256 values:

    e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
    fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c

## 1. Provider atoms

Let \(R_\phi\), \(\phi\in\{0,1\}\), be the exact incumbent reservation maps:
20 rows in each phase, 17 shared rows, and 23 rows in their union. Private
rows and rows in \(\operatorname{dom}R_\phi\) are unavailable in phase
\(\phi\). A row reserved only in the other phase is available only at its
other-phase incumbent flag. The ten materialized incumbent LLR hosts remain
valid long providers.

A phase-\(\phi\) provider atom is either:

* \(B_\phi(v,a)\), an admissible flagged state of a parent long row \(v\); or
* \(H_\phi(y,a)\), the flagged long state installed at host row \(h_y\) by
  selected mode \(y\).

Each atom records its physical row, flag, literal long family, and the
phase-specific root and owner data used by the exact transition predicates.
For a selected endpoint-disjoint mode set \(I\), the provider bank is

\[
 {\cal P}_I^\phi=
 \{B_\phi(v,a):v\notin\{d_y:y\in I\}\}
 \cup\{H_\phi(y,a):y\in I,\ 0\le a<4\}.                \tag{1.1}
\]

The base atoms in (1.1) are already filtered by the private and reservation
rules. Fixed-bank safety makes every selected host admissible.

For role \(x\), phase \(\phi\), and declared key
\(k=(q,\alpha,\beta)\), let \({\cal A}_x^\phi(k)\) be the ordered atom
pairs \((\xi,\eta)\) satisfying the exact incoming, outgoing, and common
five-cell predicates for the new short of \(x\), at flags
\(\alpha,\beta\). If both atoms use one physical row then
\(\alpha=\beta\). For \(I=\{e,f,g\}\),

\[
 \boxed{
 {\cal T}_x^\phi(k;I)
 ={\cal A}_x^\phi(k)\cap({\cal P}_I^\phi)^2.}           \tag{1.2}
\]

This equality is the lossless donor-delete/host-insert factorization.

## 2. Finite directed support patterns

For a chosen phase tuple \(t_x^\phi\), define

\[
 m_{xy}:=\{\phi\in\{0,1\}:h_y\in\operatorname{row}(t_x^\phi)\},
 \qquad x,y\in\{e,f,g\}.                               \tag{2.1}
\]

Thus \(m_{xy}\) is the phase mask of arc \(x\to y\); loops record own-host
use.

### Lemma 2.1 (external-host necessity)

If \(e\) is one of the 468 authenticated H sources, every two-phase option
for \(e\) in an endpoint-disjoint triple satisfies

\[
 m_{ef}\cup m_{eg}\ne\varnothing.                      \tag{2.2}
\]

#### Proof

The unary child for \(e\), with \(d_e\) deleted and \(h_e\) installed, has
no two-phase option. Adding \(f,g\) only deletes \(d_f,d_g\) and inserts
\(h_f,h_g\). A triple option using neither helper host avoids the two deleted
rows and hence was already a unary option. Deletion cannot create a tuple,
a contradiction. \(\square\)

Ignoring phases, loops, and base providers, there are exactly

\[
 3\cdot2^4=48                                          \tag{2.3}
\]

external-support digraphs: \(N^+(e)\cap\{f,g\}\) is one of
\(\{f\},\{g\},\{f,g\}\), while the four arcs
\(f\to e,f\to g,g\to e,g\to f\) are arbitrary. Adding three loop bits gives
384 raw unphased support graphs. These are class labels, not claims that all
are physically realizable.

There is an exact phase-capacity count. In one phase, each of the three host
rows is unused or assigned to one of three roles: \(4^3=64\) assignments.
A tuple has only two provider positions, so remove the three assignments
giving all hosts to one role. This leaves 61. If neither external host is
assigned to source \(e\), there are \(4\cdot3\cdot3=36\) assignments, minus
the all-to-\(f\) and all-to-\(g\) cases, hence 34. Across two phases, (2.2)
therefore leaves

\[
 \boxed{61^2-34^2=2565}                                \tag{2.4}
\]

phase-labelled host-incidence matrices. Nonhost capacity and flag consistency
remain join predicates.

## 3. Complete natural-join theorem

For each unordered triple meeting H, choose
\(e=\min(I\cap H)\) as canonical H anchor and order the other modes \(f<g\).
For a tuple \(t\), let \(F(t)\) be its physical footprint and
\(\gamma_t\) its row-to-flag map.

For one of the 2,565 matrices \(M\), define \({\cal J}_M\) to consist of

\[
 (e,f,g,k_e,k_f,k_g,
 t_e^0,t_e^1,t_f^0,t_f^1,t_g^0,t_g^1)                 \tag{3.1}
\]

satisfying:

1. \(e=\min(\{e,f,g\}\cap H)\), \(f,g\) are fixed-bank-safe, and \(f<g\);
2. all six endpoint rows are distinct;
3. \(t_x^\phi\in{\cal T}_x^\phi(k_x;\{e,f,g\})\) for every role and phase;
4. the host masks of the six tuples are exactly \(M\);
5. in each phase, \(F(t_e^\phi),F(t_f^\phi),F(t_g^\phi)\) are pairwise
   disjoint;
6. \(\bigcup_{x,\phi}\gamma_{t_x^\phi}\) is a function.

The three role keys are independent; only the two phases of one role share a
key.

### Theorem 3.1

An endpoint-disjoint unordered triple containing an H source has a complete
three-ticket, two-phase occurrence packing if and only if it lies in

\[
 \boxed{
 {\cal D}_3=
 \pi_{e,f,g}\left(\bigcup_{M\in{\mathfrak M}_{2565}}
 {\cal J}_M\right).}                                   \tag{3.2}
\]

#### Proof

A literal packing assigns a provider atom to each predecessor/successor.
Equations (1.1)--(1.2) place all six tuples in the aperture relations. Their
host uses define a matrix in \({\mathfrak M}_{2565}\) by phase capacity, the
two-provider bound, and Lemma 2.1. The packing satisfies conditions 5--6, so
it yields a right-side join record.

Conversely, a join record supplies exact tuples from the triple banks.
Same-role keys join each role across phases; condition 5 gives phase-local
unit capacity; condition 6 gives one global physical flag address. The bank
definition already enforces private and reservation rules. Hence the six
tuples form a complete occurrence packing. \(\square\)

Equation (3.2) is the weakest exact occurrence screen: no supplier, Hall,
chronology, upper, residence, or compiler condition is imposed.

## 4. Indexed host-aperture enumeration

The domain (3.2) need not be evaluated through the blind outer loop

\[
 468\times112621^2.                                    \tag{4.1}
\]

Give every host atom the exact signature

\[
 \Sigma_\phi(y,a)=
 (\phi,a,\text{long family at }h_y,
 \text{phase root at }h_y,\text{phase owner at }h_y). \tag{4.2}
\]

The displayed \(\Sigma_\phi\) is only an index bucket key. Every posting in
that bucket must retain the installing mode \(y\), physical host row \(h_y\),
donor \(d_y\), tuple side, complete physical footprint, and flag map; equal
value signatures never coalesce physical atoms.

Index \({\cal A}_x^\phi(k)\) by role, phase, key, provider kinds, the one or
two external-host signatures, residual base-row footprint, and flag map. A
base atom carries its row as a kill label and survives exactly when that row
is not \(d_e,d_f,d_g\). Every aperture record has arity at most two.

Lemma 2.1 supplies a join anchor: every output has a source aperture using
\(h_f\) or \(h_g\). Evaluate the join as follows.

1. Enumerate directed source-to-helper aperture postings, not helper pairs.
2. If a source option uses both helpers, bind both through one two-host
   posting or through two one-host postings joined on source key and flags.
3. If it uses one helper, bind that helper first and retrieve the second from
   the indexed relations required by the remaining five tuples.
4. Intersect endpoint, donor-kill, phase-footprint, and flag postings before
   emitting the helper pair.

This is exact and retains all alternative tuples. It avoids materializing a
helper-pair square whose members have no matching aperture record. The 48
off-diagonal graphs are a coarse join partition; the 2,565 matrices are its
complete literal-capacity refinement.

## 5. Sharp output-size limitation

No lossless result can promise subquadratic worst-case output from unary
emptiness alone. Take \(N\) helpers with distinct endpoints, identical
compatible host signatures, donors unused by every selected tuple, and
enough private base rows for all capacities. Give the source an option using
the host of either selected helper and every helper a private base option.
Every unordered helper pair then lies in \({\cal D}_3\).

There are \(\binom N2\) genuine outputs, so explicit exact enumeration needs
\(\Omega(N^2)\) output time. The gain from (3.2) is output sensitivity, not
an unconditional subquadratic guarantee: avoid blind triple materialization
but retain every indexed-join survivor.

## 6. Downstream scope

For each triple emitted by (3.2), retain one complete six-tuple witness and
its global flag map, jointly materialize all three transfers, and replay the
complete supplier matching. Only then test chronology, residence, arbitrary
upper coverage, and the compiler.

A negative join is an exact occurrence no-go. A positive join is a complete
three-mode occurrence certificate, not a supplier contraction or K17 word.
