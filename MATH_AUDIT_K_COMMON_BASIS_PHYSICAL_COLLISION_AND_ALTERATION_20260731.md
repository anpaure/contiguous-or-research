# Independent audit of the common-basis physical collision and alteration theorems

Date: 2026-07-31  
Verdict: GO, with the scope restrictions stated below

## 1. Sources audited

The load-bearing sources, at the time of this audit, are:

1. MATH_THEOREM_K_BALANCED_COMMON_BASIS_PHYSICAL_COLLISION_BARRIER_20260731.md,
   SHA d9d21a3123f13cc935944dc326f8bad99ea47586453c5a974f6f120675ba9829;
2. MATH_THEOREM_K_COMMON_BASIS_PRIVATE_CIRCUIT_ALTERATION_20260731.md,
   SHA 5e2702b3c354aa8de2e29625183f44244270b7b67c2bd034514b634dc1a71767;
3. MATH_THEOREM_K_LOGDEGREE_PHYSICAL_SIDE_FOREST_CUT_OBSTRUCTION_20260731.md.

The third source received only wording/tail-bound corrections during this
audit; its final hash is recorded in the handoff after freezing.

The audit is mathematical.  No conclusion below treats a finite search as
an all-dimensional proof.

## 2. Off-central BTK calculation

For one side let

\[
 M=\binom{2n}{n},\qquad
 N=\binom{2n}{n+1}=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n+2}.
\]

In the standard BTK two-step matching, let \(q(W)\) count how many selected
diamonds use \(W\) as their opposite rank-\((n+1)\) corner.  The
minimum-return decomposition gives

\[
 F_j(z)
 =(zC(z))^j\sum_{a\ge0}z^aC(z)^{2a+2}
 ={z^jC(z)^{j+1}\over\sqrt{1-4z}}.
\]

Using

\[
 [z^s]{C(z)^b\over\sqrt{1-4z}}=\binom{2s+b}{s}
\]

at \(s=n-j-1\), \(b=j+1\), gives exactly

\[
 |\{W:q(W)=j\}|=\binom{2n-j-1}{n-j-1}.
\]

The histogram sums to \(N\), while its first moment is \(P\).  The first
two nontrivial checks are

\[
\begin{array}{c|c|c|c}
n&(c_0,c_1,\ldots)&\#\{q\ge3\}&
 \sum(j-2)_+c_j\\ \hline
4&(35,15,5,1)&1&1\\
5&(126,56,21,6,1)&7&8.
\end{array}
\]

Two hockey-stick summations give

\[
 \#\{q\ge3\}=\binom{2n-3}{n-4},
\qquad
 \sum_W(d(W)-2)_+\ge\binom{2n-2}{n-4}.
\]

The ratios to \(N\) tend respectively to \(1/8\) and \(1/4\).  Orienting
each lifted edge from its on-chain corner to its opposite corner strictly
increases the coordinate-sum potential.  Since on-chain tails are
distinct, the orientation has outdegree at most one; an undirected cycle
would then force a directed cycle.  Hence this BTK side graph is acyclic:
the obstruction is pure branching overload.

Coordinate symmetrization is transitive on all containments
\(L\subset U\), and every matching uses \(P\) of the
\(P\binom{n+2}{2}\) incidences.  Its atom marginal is therefore exactly

\[
 \theta={1\over\binom{n+2}{2}}.
\]

Thus exact saturation and exact uniform atom marginals genuinely coexist
with the displayed \(\Theta(N)\) overload.  This is a one-shore diagonal
basis; compatibility with the tail complement of a prescribed child
common basis is not asserted.

Deleting one selected diamond lowers
\(\Omega_2=\sum(d-2)_+\) by at most two.  Therefore every cap-two
replacement changes at least

\[
 {1\over2}\binom{2n-2}{n-4}
\]

diamonds.  A C6 toggle deletes three old diamonds and lowers the potential
by at most six, yielding the stated one-sixth switch floor.  A long
alternating circuit does not evade the total removed-support bound.

## 3. Random-law and anchor checks

For a physical star \(W\), compatible \(k\)-sets number

\[
 A_k=k!\binom{n+1}{k}\binom{n-1}{k}.
\]

The identity

\[
 \binom d3^2
 =\binom d3+12\binom d4+30\binom d5+20\binom d6
\]

is exact.  Under the stated six-local cylinder hypothesis it gives, by
the second-moment inequality,

\[
 \Pr(d(W)\ge3)\ge
 { (1-\varepsilon)^2(A_3\theta^3)^2\over
   (1+\varepsilon)(A_3\theta^3+12A_4\theta^4+
                   30A_5\theta^5+20A_6\theta^6)}.
\]

Since \(A_k\theta^k\to2^k/k!\), the limit is \(4/43\).  This is conditional
on local product behaviour; it is not attributed to the unknown uniform
Boolean perfect-matching law.

For a physical graph fixed independently of the balanced common basis,
the anchor identity

\[
 \mathbb E\sum_{W\in B}(d_G(W)-1)_+
 ={C\over N}\sum_W(d_G(W)-1)_+
\]

is exact, with bounds

\[
 C{n-4\over n+2}\le\mathbb EA_B(G)<2C.
\]

It is only an additive diagnostic: the frozen graph need not be feasible
for every puncture.  For an adaptive \(G_Q\), the missing information is
the covariance between anchor membership and \(d_{G_Q}\).  The stated
two-point decorrelation hypothesis correctly restores the upper bound
\(2\Lambda C\).  Once both side graphs are forests, the contracted seam
graph has only \(2C\) seam edges and hence cycle rank at most \(2C\).

## 4. Alternating-circuit theorem

Contracting a fixed perfect matching turns each nonmatching incidence into
a directed arc.  Directed cycles are exactly matching-alternating
circuits, and the symmetric difference of two perfect matchings is a
vertex-disjoint family of such circuits.  Thus long circuits are a
complete move language at fixed \(Q\); directed triangles, equivalently
C6 moves, need not be complete.

After deleting the old halves, the physical test is exact: the residual
must be a forest, the new endpoint degrees must obey the ordinary and
anchor caps, and the new links must be loopless and graphic-independent
after component contraction.  This also tests the final contracted
\(\Gamma_Q\) row.

Under the explicitly private/common-off hypotheses, choosing one repair
link per token is a Rado independent-transversal problem in a graphic
matroid.  Hence all tokens are repairable exactly when

\[
 r_{\rm gr}\!\left(\bigcup_{i\in J}L_i\right)\ge|J|
 \qquad(J\subseteq I).
\]

The deficient Rado formula

\[
 \max\#\hbox{ repaired}
 =\min_{J\subseteq I}
 \left(|I\setminus J|+
 r_{\rm gr}\!\left(\bigcup_{i\in J}L_i\right)\right)
\]

is correct.  A rank lower bound
\(r_{\rm gr}\ge\alpha|J|-\beta\) therefore gives

\[
 V'\le(1-\alpha)V+\beta.
\]

The fixed-tree list-pressure corollary is also exact: if every surviving
list has at least \(\lambda\) distinct tree edges and every tree edge has
pressure at most \(\mu\), then the graphic rank is at least
\((\lambda/\mu)|J|\).

The common-basis puncture-survival theorem is a valid use of one-point
marginals.  To pass from raw corridor survival to graphic rank, however,
one must designate one corridor per distinct link and require the
component-tree labels to remain valid for every allowed \(Q\).  These
requirements are now explicit.  Under them, risk length \(L=o(n)\) and a
fixed pressure gap give

\[
 V'\le {2(C/N)L\over\varepsilon}V=o(V);
\]

for \(V=O(N)\), \(L=O(1)\), the remainder is \(O(\operatorname{Cat}_n)\).

Private off packets on two shores contain at most \(2P\) old matching
edges in total.  Therefore circuits using at least \(s\) old edges can
service at most \(2P/s\) separate tokens.  Generic length-\(\Theta(n)\)
absorbers are necessarily only a Catalan-scale final bank unless one
circuit repairs many tokens.

## 5. Off-centre absorber

The explicit monotone-geodesic construction for ranks \(r\) and \(r+2\)
passes.  Under \(|L\setminus U|\ge3\), arbitrary prescribed first upper
and last lower incidences extend to an alternating endpoint path of length
at most \(2r+3\), with distinct lifted rank-\((r+1)\) vertices in each
state.  The case \(r=4\) is vacuous; \(r=5\) is the first nonvacuous case.

The collision proof uses the first inserted element \(b_1\) to separate
the start, the final unswapped element \(a_*\) to separate the finish, and
two filler exclusions for adjacent transition unions.  The discarded
claim that every internal base retains \(p\) was false but unused.  An
independent clean replay checked 11,926 admissible instances for
\(r=5,\ldots,9\) without a collision.

Two internally outer-disjoint, physically cross-disjoint endpoint paths
do form one literal long alternating circuit.  The single-path theorem
does not itself prove that two arbitrarily prescribed paths can be packed
disjointly, nor that their lower vertices survive the common-basis
puncture.

## 6. Abstract cut obstruction

The logarithmic-degree construction is sound.  Each tight block forces
\(|W|\) selected physical edges inside \(|W|\) sockets.  If degree exceeds
two, the cap row fails; otherwise every socket has degree two and a cycle
is forced.  The fractional incidence point respects every socket degree
capacity but violates the tight graphic inequality by exactly one.  The
construction therefore proves the necessity of cutwise graphic expansion,
not a failure of a fractional state which already satisfies all graphic
cuts.

The paired-module construction has degree \(\Theta(m)\), codegree
\(O(m^{1/3})\), surplus \(\Theta(Nm^{-2/3})\), and
\(m=\Theta(\log N)\).  Any enlargement must select a new cross-cut atom
touching each tight module, so at least \(\lceil t/2\rceil
=\Theta(N/\log N)\) selected new atoms are necessary.  This is an
abstract representative system, not a Boolean containment counterexample.

## 7. Proved boundary

The following inference is now rigorously closed:

\[
\text{balanced common-basis marginals}
\ \Longrightarrow\
O(\operatorname{Cat}_n)\text{ random physical repair}.
\]

It is false.  Marginals and locally product representative laws permit
\(\Theta(N)\) overload.

The positive conditional theorem is exact: a \(Q\)-robust, node-private,
common-off circuit atlas routed to a fixed component forest and satisfying
the graphic Rado cuts yields contractive alteration, with the explicit
coefficient above.  What remains unproved for the Boolean recursion is the
existence of that correlated atlas, or an equivalent direct cap-two
representative selection.  No obstruction here rules out such a structured
construction, and no claim about the full contiguous-OR formula follows.
