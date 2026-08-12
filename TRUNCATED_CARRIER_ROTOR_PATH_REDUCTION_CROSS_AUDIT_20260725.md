# Cross-audit of the truncated carrier-rotor path reduction

Date: 2026-07-25

Audited source:

* `TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_20260725.md`.

## Verdict

**The main sufficient reduction is valid after one local repair and two
semantic qualifications.**  The physical MTF compilation, carrier
invariance, regular quotient rotor, stationary one-time flag marginals,
primary length ledger, tail ledger, and implication `(TRP) => constant one`
all check out.

The required changes are:

1. A carrier state is a **truncated quotient state**: it specifies the first
   `2Q+1` exact MTF blocks and only the union of the remaining tail blocks.
   After the first rotor update the displayed tail is generally not one exact
   block.  Formula (1.2) is nevertheless the exact induced recurrence on this
   quotient, and every quotient path compiles literally.
2. Equations (4.1)--(4.2) are exact for **occurrence multiplicities**.  They
   are not, without a no-self-collision estimate, an exact fractional load in
   the ordinary set-incidence hypergraph whose edge records whether a target
   occurs at least once on a path.
3. At the endpoint `q=H`, the upper member of a full packet is the carrier
   `U` itself, repeated at all starts.  Its hit probability is `1/N_H`, not
   `M/N_H`.  Thus (5.1) is false as displayed at this one signed endpoint.
   The repair is harmless because `N_H=O(W/m)=o(W)`: omit that endpoint from
   the reservoir estimate and repair all rank-`M` targets literally.

The claim that cyclic packets form a subfamily is correct, but the source
does not prove it.  An explicit embedding is given in Section 7 below.

No earlier deterministic obstruction disproves `(TRP)`.  However, the
isolated-reset ABKV ceiling applies exactly to any attempt to treat a whole
length-`M`, radius-`Q` path as one ordinary ABKV atom.  Its uniformity is at
least `M` and naturally `M(2Q+1)`, while an unavoidable nested-pair relative
codegree is `Omega(1/m)`.  The ABKV hypothesis fails overwhelmingly.  Thus
`(TRP)` requires a new correlated path-selection theorem; it is not obtained
by the existing queue/ABKV black box.

## 1. Crossing and length scales

Let

\[
 \lambda_h=\frac{W}{N_h},\qquad M=m+H,
\]

and let `H` be the first index with `lambda_H >= m+H`.  The standard central
binomial expansion gives

\[
 \log\lambda_h=\frac{h^2}{m}
 +O\!\left(\frac hm+\frac{h^3}{m^2}\right),
\]

uniformly at the crossing.  Hence

\[
 H=(1+o(1))\sqrt{m\log m}.
\]

Minimality and

\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{m+H}{m-H+1}
\]

give

\[
 1-O(H/m)\le \frac{MN_H}{W}\le1.
\]

Therefore

\[
 T:=MN_H=W-O(WH/m)=W-o(W),
 \qquad HN_H=O(WH/m)=o(W).
\]

For

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma)}\right\rceil,
 \quad \gamma\to\infty,
 \quad \gamma=o(\log\log m),
\]

one has `Q=o(H)`, and both `m-Q` and `H-Q` tend to infinity.  Apart from the
typographical `quad` in the source, Section 0 is correct.

## 2. Exact MTF recurrence: quotient, not a single tail block

At initialization the exact ordered partition is

\[
 \Sigma=(L,\{z_1\},\ldots,\{z_{2Q}\},R),
 \qquad
 R=R_U\sqcup([2m]\setminus U).
\]

Append

\[
 A=L-x+y,qquad x\in L,\ y\in R_U.
\]

The exact MTF recurrence produces the prefix

\[
 A,\{x\},\{z_1\},\ldots,\{z_{2Q}\},
\]

followed by the old tail partition with `y` deleted.  In particular,
`z_{2Q}` does **not** literally merge with the remaining tail.

If one retains only the first `2Q+1` blocks

\[
 A,\{x\},\{z_1\},\ldots,\{z_{2Q-1}\}
\]

and records the union of everything after them, then the carrier part of
that tail union is exactly

\[
 R_U-y+z_{2Q}.
\]

Thus the induced quotient recurrence is exactly

\[
 (L;z_1,\ldots,z_{2Q};R_U)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R_U-y+z_{2Q}).
\]

This is formula (1.2).  The correct wording is therefore:

> a carrier state specifies an exact MTF prefix and an unresolved tail
> union, not necessarily one final exact block.

This correction does not weaken composition.  Given any refinement of the
tail union, every `y in R_U` can be inserted in the next mask.  Deleting it
wherever it lies in the exact tail leaves precisely the quotient successor
above.  Coordinates outside `U` are never inserted into a prefix mask, so
they remain in the unresolved tail forever.  Hence `U` is exactly invariant
along every quotient path.

## 3. Regularity and connectivity

The outdegree is

\[
 d=(m-Q)(H-Q).
\]

For a proposed successor

\[
 (L';w_1,\ldots,w_{2Q};R_U'),
\]

choose `y in L'` and `z in R_U'`.  The unique predecessor is

\[
 L=(L'-y)+w_1,
\]

\[
 (z_1,\ldots,z_{2Q})=(w_2,\ldots,w_{2Q},z),
\]

\[
 R_U=(R_U'-z)+y.
\]

This gives the same indegree `d`.  The state count

\[
 |\Omega_Q(U)|=\frac{M!}{(m-Q)!(H-Q)!}
\]

is also exact.

The slot argument proves weak connectivity of the quotient graph.  In the
underlying undirected graph, inverses of rotor slot cycles may be used; with
the stabilizers of the unordered `a`- and `b`-slots they generate a
transposition between an `a`-slot and `q_1`, then all adjacent
transpositions along a rotor cycle, and hence the full symmetric group on
the slots.  Since the finite digraph is balanced at every vertex, each weak
component is strongly connected.  Section 1 therefore passes once “last
block” is replaced by “tail union.”

## 4. Flag exposure and the averaged owner kernel

Every exact representative of a quotient state begins with

\[
 L,\{z_1\},\ldots,\{z_{2Q}\}.
\]

Consequently the cumulative prefix unions are literal suffix ORs at that
endpoint, and (2.1)--(2.3) have the claimed ranks.

At the successor,

\[
 X'=(L-x+y)+x+z_1+\cdots+z_{Q-1}=X-z_Q+y.
\]

Conditioned on a **uniform** quotient state with owner `X`, the ordered
`Q`-tuple in `X`, the ordered `Q`-tuple in `U-X`, and the two unordered
remainders are uniform and independent.  Averaging also over a uniform
choice of `(x,y)` gives

\[
 \Pr(X'=X-a+b\mid X)=\frac1m\frac1H.
\]

This is correct as a stationary averaged statement.  It is not a statewise
claim: at a fixed state, the deleted owner coordinate is the fixed `z_Q`,
and only `H-Q` choices of the added coordinate are currently available.

## 5. Literal compilation and primary cost

Writing

\[
 R,\{z_{2Q}\},\ldots,\{z_1\},L
\]

does initialize the exact partition with the required prefix.  It costs
`2Q+2` nonzero letters.  Every later quotient edge is compiled by the one
letter `L-x+y`, independently of the current refinement of the tail.
Therefore a walk with `s` state endpoints costs

\[
 2Q+2+(s-1)=s+2Q+1
\]

and exposes its entire radius-`Q` flag at every endpoint.

Taking `s=M` for each of the `N_H` carriers costs

\[
 MN_H+(2Q+1)N_H
 =T+O(QW/m)=W+o(W).
\]

It is safer throughout to say “directed walk.”  Repeated quotient states are
physically allowed.  If “path” is intended to mean simple path, existence is
still not an issue because the cyclic subfamily supplies a simple
length-`M` trajectory.

## 6. Stationary flag loads: exact multiplicity, not exact support

Uniform outgoing transition on the regular quotient digraph has uniform
stationary distribution.  A uniform initial state therefore makes every
time marginal uniform.  Coordinate transitivity inside a fixed carrier
then gives, for every `r=m+-q`, `q<=Q`,

\[
 \Pr(F_r(\omega_t)=S\mid S\subset U)=\binom Mr^{-1}.
\]

Summing over the carriers containing a fixed `S` yields

\[
 \binom{2m-r}{M-r}\frac{M}{\binom Mr}
 =\frac{MN_H}{\binom{2m}r}.
\]

Thus (4.1)--(4.2) are exact for the expected **number of endpoint
occurrences** of `S`.

They are not automatically the incidence degree in the ordinary path
hypergraph, because one path may visit the same target more than once.  In
that hypergraph an edge contributes only one to the support indicator of a
target, whereas (4.1) counts all visits.  The source's actual open condition
`(TRP)` correctly uses support unions, so the sufficient theorem is not
affected.  But a later rounding argument may not cite (4.2) as a fractional
perfect cover without either:

* restricting to paths with no same-rank self-collisions; or
* proving that the total self-collision loss is `o(W)`.

There is a rigorous independent-choice obstruction already at `q=0`.
For a fixed middle owner `X`, let `p_U` be the probability that the random
walk chosen in a carrier `U superset X` visits `X`.  Then

\[
 p_U\le \frac{M}{\binom Mm},
\]

and

\[
 \sum_{U\supset X}p_U\le \frac{T}{W}=1-o(1),
 \qquad \max_U p_U=o(1).
\]

For paths chosen independently across carriers,

\[
 \Pr(X\text{ is missed})
 =\prod_{U\supset X}(1-p_U)
 \ge \exp(-1-o(1)).
\]

Hence independent stationary paths leave `Omega(W)` middle owners missing.
The final sentence of the source is therefore correct in conclusion; the
argument above makes it rigorous without assuming a Poisson limit.

## 7. Cyclic packets really are rotor trajectories

Let

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

be a cyclic order on `U`, with indices modulo `M`.  Put

\[
 B_j=\{u_j,u_{j+1},\ldots,u_{j+H-1}\},
 \qquad X_j=U\setminus B_j.
\]

Define a quotient state by

\[
 z_t^{(j)}=u_{j+H+Q-t}\quad(1\le t\le Q),
\]

\[
 z_{Q+t}^{(j)}=u_{j+H-t}\quad(1\le t\le Q),
\]

\[
 L_j=X_j\setminus\{z_1^{(j)},\ldots,z_Q^{(j)}\},
\]

\[
 R_{U,j}=B_j\setminus
 \{z_{Q+1}^{(j)},\ldots,z_{2Q}^{(j)}\}.
\]

Choose

\[
 x_j=u_{j+H+Q}\in L_j,
 \qquad y_j=u_j\in R_{U,j}.
\]

Direct substitution in (1.2) gives

\[
 \mathcal R_{x_j,y_j}(\omega_j)=\omega_{j+1}.
\]

Moreover,

\[
 L_q(\omega_j)=\{u_{j+H+q},\ldots,u_{j-1}\},
\]

and

\[
 U_q(\omega_j)=\{u_{j+H-q},\ldots,u_{j-1}\},
\]

which are precisely the cyclic intervals of ranks `m-q` and `m+q` in
that packet (up to the harmless choice of orientation/start convention).
Thus every cyclic hard-band packet is a carrier-rotor trajectory.

The rotor family is genuinely larger.  Its quotient outdegree is
`(m-Q)(H-Q)`, and the number of simple length-`M` rotor paths is already far
larger than the number of cyclic orders: at each step fewer than `M`
previous states are forbidden while

\[
 (m-Q)(H-Q)\gg M.
\]

Thus the “strict subfamily” conclusion is correct, although “two
orientations after the owner family is fixed” is unnecessary and is not
proved in the source.

## 8. Reservoir correction

For every proper rank `0<r<M`, a full cyclic packet contains `M` distinct
rank-`r` intervals.  Symmetry therefore gives hit probability

\[
 \frac{M}{\binom{2m}r}.
\]

This verifies the reservoir calculation for both signs when `q<H`, and for
the lower sign at `q=H`.

For the upper sign at `q=H`, however, `r=M`.  All `M` starts expose the same
set, namely the carrier `U`.  A uniform packet hits a fixed top with
probability

\[
 \frac1{N_H},
\]

not `M/N_H`.  The corrected residual estimate is, for example,

\[
 2\sum_{q=Q+1}^{H-1}N_q
 \left(1-\frac{M}{N_q}\right)^{R_{\rm res}}
 +2N_H=o(W).
\]

The first term is `o(W)` because

\[
 R_{\rm res}M/N_Q
 =\varepsilon W/N_Q
 \ge \log m\,e^{\gamma/2-o(1)}.
\]

The second is `o(W)` because `N_H<=W/M`.  The reservoir cost remains

\[
 R_{\rm res}(M+O(H))=o(W).
\]

Finally, since

\[
 \frac{N_{q+1}}{N_q}
 \le\frac{m-H}{m+H+1}\qquad(q\ge H)
\]

and `N_H<=W/M`, a geometric sum gives

\[
 \sum_{q>H}N_q=O(W/H).
\]

The empty set at the very end of the lower tail is simply omitted, as the
model covers nonempty masks.  Thus the repaired Section 5 passes.

## 9. The sufficient theorem

Assume `(TRP)`.  The primary compiled words have length `W+o(W)` and cover
all but `o(W)` targets in the signed rows through `Q`.  The corrected
reservoir leaves `o(W)` targets over `Q<q<=H`; literal repair costs `o(W)`.
The two tails cost `o(W)`.  Concatenation cannot destroy internal interval
witnesses.  Hence

\[
 \nu(2m)\le W+o(W).
\]

The trimmed one-bit lift has length twice the even word, while
`W(2m+1)=(2-o(1))W(2m)`, so it transfers the leading constant to odd
dimensions.  Section 6 is therefore valid after the reservoir endpoint
repair.

## 10. Which old obstruction still applies?

### 10.1 Reset accounting does not kill `(TRP)`

There are `N_H` separately initialized paths, each with `M` centers and
radius `Q`.  Their reset overhead is

\[
 (2Q+1)N_H=O(QW/m)=o(W).
\]

Thus the purely physical isolated-reset requirement `Q/M=o(1)` is
satisfied.  The common-backbone theorem is also respected: every primary
center reaches the full radius `Q`, and the separate reservoir begins only
where

\[
 N_Q/W=\exp(-Q^2/m+o(1))=o(1).
\]

The portal-depletion theorem for repeatedly spliced fresh canonical queue
components is not in scope.  A carrier path is one continuous quotient MTF
trajectory, and it allows the exact tail to refine while retaining only its
union.  It pays one initialization and has no internal seam.

### 10.2 Direct ABKV rounding is decisively excluded

If a whole path is made one full multirank atom, its natural real-slot
uniformity is

\[
 K=M(2Q+1).
\]

Even an owner-only atom has uniformity `M`.  In any near-regular full-slot
system, every lower-row incidence has a same-endpoint middle superset.
Double counting nested pairs gives the same unavoidable scale as in the
isolated-reset audit:

\[
 \frac{C}{D}\ge\frac{1-o(1)}m.
\]

The ABKV hypothesis

\[
 e^{2K}C\log D=o(D)
\]

would force `K<=(1/2+o(1))log m`.  Here

\[
 M\asymp m,
 \qquad Q^2\asymp m\log\log m,
\]

so the condition fails already for the owner-only uniformity, and a
fortiori for `M(2Q+1)`.

Equivalently, the audited isolated-reset queue ceiling says that a direct,
unsplit full-radius ABKV certificate with negligible reset overhead must
satisfy

\[
 Q^2=o(\log m),
\]

which is maximally incompatible with the present `Q`.

This does **not** prove `(TRP)` false.  It says that the extra dynamic path
freedom has not yet been converted into a valid rounding theorem.  A proof
must exploit sequential dependence, an object-specific discrepancy method,
or a correlated global reconfiguration; treating each complete path as an
independent hyperedge falls back inside the already closed ABKV
architecture.

## Final calibrated status

After the corrections above, `(TRP)` is a legitimate and strictly weaker
sufficient target than the cyclic-packet selection theorem:

* literal factorization is exact;
* the carrier is invariant;
* all one-time state/flag marginals are exactly uniform;
* the primary, reservoir, and tail costs are `W+o(W)`;
* cyclic packets embed explicitly as rotor trajectories.

What remains completely open is the support-level, correlated selection of
one length-`M` path per carrier with `o(W)` total hard-row holes.  Neither
independent stationary paths nor the existing queue/ABKV theorem provides
it.

The later automorphism-overlay audit
`MATH_ATTACK_TRUNCATED_CARRIER_ROTOR_ACD_20260725.md` further separates the
dynamic freedom. Owner-fixed branching is rigorously boundary-only: all
interior depth-`q` flags are determined by consecutive owner paths, so two
lifts of one owner sequence differ in only `O(q)` occurrences. The only
remaining possible macroscopic mechanism is a second legal rotor path
factor on essentially the same owners with linearly different successor
structure. Strong connectivity and large quotient outdegree do not prove
that rethreading statement.
