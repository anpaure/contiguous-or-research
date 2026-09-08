# Re-audit of the revised correlated-row nested-charge and literal-escape note

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Audited report:

- MATH_ATTACK_L_CORRELATED_ROW_NESTED_CHARGE_BARRIER_AND_LITERAL_ESCAPE_20260726.md,
  revised version of 2026-07-26.

Source checks:

- MATH_THEOREM_CORRELATED_ROW_ORBIT_ABSORBER_AND_SHADOW_LOCK_20260726.md;
- MATH_THEOREM_N_OUTER_OWNER_FLAG_RUN_INVARIANT_20260726.md;
- MATH_THEOREM_N_H_MEMORY_KERNEL_SHADOW_UNLOCKING_20260726.md;
- MATH_THEOREM_O_TERNARY_CARRY_DIRECT_COMPILER_AUDIT_20260726.md;
- MATH_ATTACK_N_PRODUCT_SCD_TAIL_UNIFORM_ASYMPTOTIC_20260726.md;
- MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md.

## 0. Final verdict

The revised report has correctly incorporated the substantive corrections
from the first audit:

1. the \(H=o(m^{1/3})\) gain remains explicitly conditional on nested
   charging;
2. the SCD statement now says “need not satisfy,” rather than claiming
   universal violation of the run equations;
3. the asymptotic duplicate-bank formula now assumes \(H\to\infty\);
4. the fractional-transversal proposition now assumes target
   vertex-transitivity;
5. trace support is separated from literal compilation;
6. partial collars, full collars, and singleton repairs have separate
   exact ledgers;
7. the middle leave cancels correctly in the even near-factor formula;
8. the even and odd parity ledgers are no longer conflated.

The principal even-dimensional results are valid. In particular,

\[
 \boxed{
 L_{\rm even}\le
 W+HK+\sum_C\sigma_C
 +2\sum_C\sum_{q=1}^H(q-\sigma_C)_+}              \tag{0.1}
\]

and

\[
 \boxed{
 \nu(2m)\le
 W+E_0+2HK+\Delta_H+L_m(m-H-1)}                   \tag{0.2}
\]

are exact upper bounds under their stated compiled-cycle hypotheses.

The odd arithmetic in (8.18)--(8.22) is also correct, conditional on the
standard hypotheses made explicit in Section 7 below.

The current version also resolves the two residual scope points from the
intermediate revision:

- even compiler safety is now defined sharply as \(G_H+P_H\);
- odd compiler safety is \(G_{H+1}\), and the odd displays explicitly
  assume an exact alternating \(X/Y\) factor, both middle-shore
  partitions, full protected-band support, and uniform deepest marginals
  where the probability bound is used.

No substantive correction remains after this re-audit. The final boundary
in Section 9 is accurate: exact terminal multiplicity closure is bypassed
after literal compilation, while the compiler-safe super-Gaussian central
support construction remains open.

## 1. Terminal ledgers and floor arithmetic

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q=W/N_q.
\]

In the cap-two regime put \(s_q=W-N_q\). Under the source preload
hypotheses, the internal duplicate count is exactly \(s_q-q\), so the
relative-orbit seam expectation is

\[
\begin{aligned}
 \mathbb EC
 &=2\sum_{q=1}^Hq\frac{s_q-q}{N_q}\\
 &=2\sum_{q=1}^Hq(\lambda_q-1)
   -2\sum_{q=1}^H\frac{q^2}{N_q}.                 \tag{1.1}
\end{aligned}
\]

Uniformly for \(H=o(\sqrt m)\),

\[
 \lambda_q-1=(1+o(1))q^2/m.
\]

Hence, when \(H\to\infty\),

\[
 \mathbb EC=(1/2+o(1))H^4/m,                      \tag{1.2}
\]

whereas the bulk row-plus-column expectation is

\[
 \mathbb EZ
 \le(1+o(1))\frac{H(H+1)(2H+1)}3
 =(2/3+o(1))H^3.                                  \tag{1.3}
\]

The constants and quantifiers in revised Section 1 are correct.

For the general floor decomposition

\[
 W=cN+r,\qquad0\le r<N,
\]

an internal path has \(W-q\) occurrences. If all loads lie in
\(\{c-1,c,c+1\}\) and \(D,E\) are the \(c+1,c-1\) families, respectively,
then

\[
 |D|-|E|=r-q.                                     \tag{1.4}
\]

A distinct \(q\)-target seam \(C\) completes the histogram if and only if

\[
 E\subseteq C,\qquad C\cap D=\varnothing.         \tag{1.5}
\]

The completed high family is

\[
 D\mathbin{\dot\cup}(C\setminus E).
\]

The two cases in Lemma 2.1 and the no-deficit extension

\[
 |D|-\sum_T(c-\ell(T))_+=r-q                     \tag{1.6}
\]

are exact. The revised wording correctly says only that a uniform
super-Gaussian theorem must handle \(r_q<q\) unless a new remainder theorem
is supplied.

## 2. Nested charging

Under the shorewise implication

\[
 C_{q,k}^{\epsilon}(a)\in D_q^\epsilon
 \Longrightarrow
 C_{H,\psi(q,k,\epsilon)}^\epsilon(a)\in D_H^\epsilon,
\]

every collision is charged to one of the \(2H\) deepest signed slots.
Uniform deepest marginals give

\[
 \Pr(\mathrm{bad})
 \le H\frac{|D_H^-|+|D_H^+|}{N_H}
 \le\frac{2H(s_H-H)}{N_H}
 <2H(\lambda_H-1).                                \tag{2.1}
\]

Thus

\[
 \Pr(\mathrm{bad})\le(2+o(1))H^3/m.               \tag{2.2}
\]

This proves the conditional \(H=o(m^{1/3})\) theorem and, at
\(H=\alpha m^{1/3}\), the existence threshold \(2\alpha^3<1\).

If \(u_H\) signed slots are uncharged, the robust estimate

\[
 \Pr(\mathrm{bad})
 \le2H(\lambda_H-1)
   +u_H\max_{q\le H}(\lambda_q-1)                 \tag{2.3}
\]

is valid, and \(u_H=o(m/H^2)\) is sufficient in the stated range.

The fixed-Gaussian remainder observation is also correct: when
\(H=\lfloor A\sqrt m\rfloor\) and \(e^{A^2}\notin\mathbb Z\),

\[
 r_H/N_H\to\{e^{A^2}\},
\]

so the raw union bound is of order \(\sqrt m\) and becomes vacuous.

## 3. SCD bank, full-orbit obstruction, and the \(m^{1/3}\) barrier

For \(d_q=s_q-q\),

\[
 d_{q+1}-d_q
 =N_q\frac{2q+1}{m+q+1}-1>0                      \tag{3.1}
\]

for all large \(m\). Exactly \(N_H\) chains of an SCD of \(2^{[2m]}\)
meet rank \(m-H\). Nested chain-index sets of sizes \(d_q\) therefore give
the abstract lower and upper banks and their chosen same-chain
descendants. The revised report correctly makes no legality claim.

Every completed cap-two high family from one exact owner successor must
obey

\[
 \widehat h_{q,v}^-
 =\frac{(m-q)s_q}{2m}
 -q\left(R_v-\frac W{2m}\right),                  \tag{3.2}
\]

\[
 \widehat h_{q,v}^++\widehat h_{q,v}^-=s_q,
 \qquad\sum_vR_v=W.                               \tag{3.3}
\]

These are necessary point equations, not a memory lift.

The no-equivariant-descendant lemma is exact. For a genuinely nested pair,
the full \(S_{2m}\)-orbit condition is equivalent to

\[
 \partial^{H-q}D_q^-\subseteq D_H^-,
 \qquad
 \nabla^{H-q}D_q^+\subseteq D_H^+.                \tag{3.4}
\]

One selected SCD descendant per target does not prove these inclusions.

With \(H=o(\sqrt m)\) and \(H\to\infty\),

\[
 \sum_{q=1}^Hd_q
 =(1/3+o(1))WH^3/m.                               \tag{3.5}
\]

The revised report has added the previously missing \(H\to\infty\)
quantifier and correctly limits the “complete” ledger to the cap-two
preload terms.

For the vertex-transitive deepest-collar hypergraph,

\[
 \tau^*=N_H/H.                                    \tag{3.6}
\]

Since \(d_H/\tau^*\sim H^3/m\), this is the sharp threshold for arguments
using only edge size, target regularity, cap cardinality, and uniform
marginals. It is not an integral blocking theorem. The revised statement
now has the necessary target-transitivity assumption.

The short-core star computation is also valid. For \(k=m\pm q\),
\(q\le H\le m^{1/3}\), choosing

\[
 r=\log_2(m/q^2)+O(1)
\]

gives a star density \(\Theta(q^2/m)\), while alternatives with common
intersection of codimension \(O(H)\) hit together with probability
\((1-o(1))p\). This remains a marginal-proof obstruction rather than a
run-compatible exact preload.

## 4. Semigroup, fractional circulation, arithmetic obstructions, and memory

For prescribed nested lower and upper flags, define

\[
 R_j(X)=\bigl(X\setminus A_j^*(X)\bigr)\cup B_j^*(X).
\]

The power-consistency criterion in revised Section 6.1 is exact. One owner
permutation realizes all prescribed flags through depth \(H\) if and only
if

\[
 R_1\in\operatorname{Sym}\binom{[2m]}m,\qquad
 R_j=R_1^j\quad(0\le j\le H).                     \tag{4.0}
\]

Necessity is \(R_j=P^j\). Conversely, the power identities make
\(P=R_1\) visit the prescribed middle endpoints, and nested one-at-a-time
deletions and additions identify their intersections and unions. Separate
integral SCD flows at the individual depths do not establish (4.0).

The root and \((H-1)\)-memory overlap equations are also an exact integral
formulation. Root mass one makes selected safe-path columns binary;
prefix/suffix conservation decomposes the selected memory edges into
directed cycles and hence defines a successor permutation.

The fractional statement is correct for every \(H\le m\). Averaging all
coordinate conjugates of one length-\(2m\) wreath cycle gives root mass
one, memory conservation, and, by target transitivity and total target
mass \(W\),

\[
 \mu_j^\pm=W/N_j.                                  \tag{4.0a}
\]

Thus the real quota box is feasible. There is no fractional Hall
obstruction; the issue is integral chronology.

### 4.1 Common run line

For two \(H\)-safe owner successors on the same root support, subtraction
of the point-margin identities gives

\[
 B_{m-j}g_j^-=-j\Delta R,\qquad
 B_{m+j}g_j^+=j\Delta R.                           \tag{4.1}
\]

Thus a run-neutral trade has zero signed point effect at all depths, but
may have a nonzero target effect in the incidence kernels.

Theorem 7.1 is an exact iff for the unrestricted safe-path catalogue. An
integer trade \(\delta\) is legal, run-neutral, and cap-feasible precisely
when

\[
 z+\delta\ge0,\quad A\delta=0,\quad M\delta=0,
 \quad D\delta=0,                                 \tag{4.2}
\]

together with the displayed signed load intervals. The fixed-fibre caveat
\(C\delta=0\), or a separately proved restricted-catalogue closure theorem,
is correctly retained.

The adjacent-depth two-marginal argument forces the alternating pivot

\[
 T\longrightarrow S\longleftarrow T'             \tag{4.3}
\]

whenever a fully locked target receives positive effect. This is
necessary, not sufficient for a memory lift.

### 4.2 Exact arithmetic obstructions

At \(m=3,H=2\),

\[
 W=20,\qquad N_2=6,\qquad c_2=3,\qquad r_2=2.
\]

Every lower depth-two target is a singleton and

\[
 \mu_2^-(\{v\})=10-2R_v.
\]

All six loads are even, whereas exact balance permits only \(3,4\).
Therefore they would all be \(4\), contradicting total mass \(20\). The
finite counterexample is exact and uses one sign only.

At full depth \(j=m-1\), all singleton loads have the common residue

\[
 \mu_{m-1}^-(\{v\})\equiv W/2\pmod{m-1}.
\]

The two balanced quotas are consecutive. If \(W\bmod 2m\ne0\), both must
occur, but they cannot share a residue modulo \(m-1\) for \(m\ge3\).
Hence exact balance forces \(2m\mid W\).

For an odd prime \(m=p\),

\[
 \binom{2p}{p}
 =2\prod_{i=1}^{p-1}\frac{p+i}{i}
 \equiv2\pmod p,
\]

so \(2p\nmid\binom{2p}{p}\). This proves the infinite full-depth
obstruction. The revised report correctly limits its scope: it has no
force in the Gaussian regime \(H=o(m)\).

### 4.3 Addition-only shadow lock

Let a demanded lower depth-\(q\) target \(T\) have every child
\(S\in\partial T\) at its depth-\((q+1)\) upper cap. Every new nested safe
flag realizing \(T\) has some such child as its enclosing
depth-\((q+1)\) target. An addition-only collar therefore exceeds a child
cap. The upper statement with \(\nabla U\) is identical.

This proves revised Section 6.4 exactly. Its scope is addition-only:
a simultaneous signed replacement may remove an old child occurrence.
The memory-kernel conditions and alternating pivot (4.3) are the correct
equations for such a replacement.

## 5. Does compiler safety construct the factor atoms?

Yes, with the corrected interpretation \(G_H+P_H\).

Let \(X_1,\ldots,X_L\) be an \(H\)-geodesic Johnson path and suppose every
internal positive coordinate run has at least \(H+1\) states. Define

\[
 A_j=\bigcap_{i=\max(1,j-H)}^{\min(L,j)}X_i,
 \qquad1\le j\le L+H.                             \tag{5.1}
\]

Then, coordinatewise,

\[
 X_i=\bigcup_{j=i}^{i+H}A_j,                      \tag{5.2}
\]

\[
 \bigcap_{i=a}^bX_i
 =\bigcup_{j=b}^{a+H}A_j
 \qquad(b-a\le H),                                \tag{5.3}
\]

and

\[
 \bigcup_{i=a}^bX_i
 =\bigcup_{j=a}^{b+H}A_j.                         \tag{5.4}
\]

Here is the exact boundary-sensitive proof.

Fix a coordinate and one of its positive state-runs \([\ell,r]\).
For an internal run, \(r-\ell+1\ge H+1\), and the atom indices containing
the coordinate are exactly

\[
 [\ell+H,r].
\]

For a run meeting the left boundary they include \([1,r]\), and for a run
meeting the right boundary they include \([\ell+H,L+H]\). Consequently,
for every \(i\in[\ell,r]\), at least one containing atom index lies in
\([i,i+H]\), proving (5.2).

If \([a,b]\subseteq[\ell,r]\) and \(b-a\le H\), then the atom-index
interval for the run meets \([b,a+H]\). For an internal run this follows
from

\[
 \ell+H\le r,\qquad
 \ell+H\le a+H,\qquad b\le r,\qquad b\le a+H.
\]

Boundary runs use the clipped intervals in (5.1). This proves the forward
inclusion in (5.3), and the reverse inclusion is immediate from the
defining intersections.

For (5.4), every coordinate present in some \(X_i\), \(a\le i\le b\),
has by (5.2) a containing atom with index in
\([i,i+H]\subseteq[a,b+H]\). Conversely, for every
\(j\in[a,b+H]\), the clipped defining interval of \(A_j\) meets
\([a,b]\); hence every coordinate of \(A_j\) lies in the state union.

Thus \((A_1,\ldots,A_{L+H})\) is a literal factor word. Deleting an empty
atom cannot destroy contiguity: it only contracts an interval containing
an OR-neutral entry.

For a cyclic row, cut at any point and copy \(\sigma\) initial owner
states. Every internal positive run of the extended path is either an
unchanged cyclic run or a boundary truncation. Hence the same construction
applies. In particular, “copying owner states” in revised Theorem 8.2 is
legitimate: the copied states are inputs to (5.1), while the emitted word
entries are the atoms \(A_j\), not the owner states themselves.

This is exactly the \(G_H+P_H\) compiler-safety definition now stated
before revised Theorem 8.1. No additional chronology assumption is being
smuggled into the atom construction.

## 6. Audit of the even partial-collar and near-factor formulas

Let cycle \(C\) have \(v_C\) owner states. After a cut and
\(\sigma_C\) copied prefix states, the input path has

\[
 v_C+\sigma_C
\]

states. Formula (5.1) emits at most

\[
 v_C+\sigma_C+H                                  \tag{6.1}
\]

atoms.

At even signed depth \(q\), a cyclic trace uses \(q+1\) owner states. Of
the \(v_C\) original cyclic starts, the extended path lacks exactly

\[
 (q-\sigma_C)_+                                  \tag{6.2}
\]

starts. This count is the same for lower and upper traces. Removing that
many occurrences can uncover no more than that many physical targets.
Appending every newly missing nonempty target costs one letter.

Summing (6.1)--(6.2) over cycles gives exactly the upper bound

\[
\boxed{
 W+HK+\sum_C\sigma_C+
 2\sum_C\sum_{q=1}^H(q-\sigma_C)_+.}              \tag{6.3}
\]

This confirms revised (8.7). Moreover,

\[
 2\sum_{q=1}^H(q-\sigma)_+
 =(H-\sigma)(H-\sigma+1),                         \tag{6.4}
\]

so bare cuts and full collars cost, respectively,

\[
 W+HK+KH(H+1),\qquad W+2HK.                       \tag{6.5}
\]

No multiplicity balancing is used: only pre-cut physical support and the
literal one-letter repair operation are needed.

### 6.1 Near-factor cancellation

Let the compiled cycles contain \(P\) middle-owner occurrences, with
\(M_0\) missing distinct middle owners and middle overload

\[
 E_0=\sum_X(\mu_0(X)-1)_+.
\]

Mass conservation gives

\[
 P=W-M_0+E_0.                                     \tag{6.6}
\]

Full collars emit at most \(P+2HK\) atoms. Appending the \(M_0\) missing
middle owners changes this to

\[
 P+M_0+2HK=W+E_0+2HK.                             \tag{6.7}
\]

If

\[
 \Delta_H=\sum_{q=1}^H(M_q^-+M_q^+)
\]

is the actual positive-depth physical defect of the full cyclic traces,
then singleton completion and the even product-SCD tail give

\[
\boxed{
 \nu(2m)\le
 W+E_0+2HK+\Delta_H+L_m(m-H-1).}                  \tag{6.8}
\]

This confirms revised (8.15). The leave \(M_0\) cancels exactly and need
not be \(o(W)\). The exact sufficient central ledger is

\[
 E_0+HK+\Delta_H=o(W).                            \tag{6.9}
\]

The product-SCD exterior word composes without a seam charge and has
length \(o(W)\) whenever

\[
 H/\sqrt m\to\infty,\qquad H\le m-1.
\]

## 7. Audit of the odd formulas (8.18)--(8.22)

Assume an odd-compiler-safe exact alternating \(X/Y\) cycle factor on
\([2m+1]\), where odd compiler safety is the explicit condition
\(G_{H+1}\), with

\[
 W_o=\binom{2m+1}{m}
\]

total \(X\)-owner states, and suppose its cyclic signed traces have full
support in the protected band. Write

\[
 Y_i=X_i\cup X_{i+1}.
\]

At depth \(q\), the lower target uses \(q+1\) consecutive \(X\)-states,
whereas the upper target uses \(q+2\). The unrestricted union identity
(5.4) is why the same delay-\(H\) atom row represents the upper
\((H+2)\)-state trace.

Choose \(0\le\sigma_C\le H+1\) copied prefix \(X\)-states. The compiler
base on cycle \(C\) is

\[
 v_C+\sigma_C+H.
\]

The unavailable cyclic starts are exactly

\[
 (q-\sigma_C)_+
 \quad\text{lower},\qquad
 (q+1-\sigma_C)_+
 \quad\text{upper}.                               \tag{7.1}
\]

At \(q=0\), a bare cut \(\sigma_C=0\) loses the wraparound \(Y\)-owner;
any \(\sigma_C\ge1\) retains it. If \(z_0\) is the number of bare cuts,
the literal central upper bound is therefore

\[
\boxed{\begin{aligned}
 L_{\rm odd}\le{}&
 W_o+HK+\sum_C\sigma_C+z_0\\
 &+\sum_C\sum_{q=1}^H
 \left((q-\sigma_C)_+
 +(q+1-\sigma_C)_+\right).
\end{aligned}}                                    \tag{7.2}
\]

This confirms revised (8.18).

For one bare cycle, the positive-depth occurrence loss is

\[
 \sum_{q=1}^H(2q+1)=H^2+2H.
\]

Including the lost \(Y\)-owner gives \((H+1)^2\). The compiler base itself
has the additional \(H\) atoms, so the total one-cycle bound is

\[
 W_o+H+(H+1)^2.                                   \tag{7.3}
\]

For full collars, \(\sigma_C=H+1\); every loss in (7.1) and \(z_0\)
vanishes. Thus

\[
 L_{\rm odd}\le W_o+(2H+1)K,                      \tag{7.4}
\]

confirming (8.19). The extra \(1\), compared with the even full collar,
comes from the \(H+2\)-state upper trace.

The odd lift of the product-SCD exterior word has length

\[
 2L_m(m-H-1)
\]

and covers exactly the ranks outside

\[
 [m-H,m+H+1].
\]

Consequently

\[
\boxed{
 \nu(2m+1)\le
 W_o+(2H+1)K+2L_m(m-H-1)}                         \tag{7.5}
\]

under the exact-factor, compiler-safety, and full-support hypotheses.
This confirms (8.20).

### 7.1 Odd floor identities

Put

\[
 N_q^o=\binom{2m+1}{m-q}
      =\binom{2m+1}{m+1+q},
\qquad
 W_o=c_qN_q^o+r_q.
\]

After one bare cut of one cyclic Hamilton row, the lower and upper
occurrence totals at depth \(q\) are

\[
 W_o-q,\qquad W_o-(q+1),
\]

respectively. If each signed load belongs to
\(\{c_q-1,c_q,c_q+1\}\), the same mass calculation as in (1.4) gives

\[
\boxed{
 |D_q^-|-|E_q^-|=r_q-q,\qquad
 |D_q^+|-|E_q^+|=r_q-(q+1).}                      \tag{7.6}
\]

This confirms (8.21). For \(K\) bare cuts, the right sides would instead
be \(r_q-qK\) and \(r_q-(q+1)K\); the revised formula is correctly stated
for one bare path.

In the odd no-deficit regime at depth \(H\), necessarily
\(r_H\ge H+1\), and the lower and upper high families have sizes

\[
 r_H-H,\qquad r_H-(H+1).
\]

If the \(H\) lower and \(H+1\) upper deepest crossing targets are uniform
under a relative shore distribution, the raw union bound is

\[
\boxed{
 H\frac{r_H-H}{N_H^o}
 +(H+1)\frac{r_H-(H+1)}{N_H^o}.}                  \tag{7.7}
\]

This confirms (8.22) with the stated relative-uniformity qualification.
It is not an unconditional odd nested-charge theorem.

## 8. Exact proved/conditional boundary after re-audit

### Proved

1. The terminal first-moment constants \(1/2\) and \(2/3\).
2. The floor/remainder seam dichotomy.
3. The conditional nested-charge improvement to \(H=o(m^{1/3})\).
4. The abstract SCD bank and the full-orbit equivariance obstruction.
5. The exact semigroup criterion, integral memory-circulation equivalence,
   and symmetric fractional feasibility.
6. The \(m=3,H=2\) parity obstruction, the odd-prime full-depth
   obstruction, and their sharply limited scopes.
7. The addition-only shadow lock.
8. The fractional \(m^{1/3}\) barrier for target-regular marginal
   arguments and the short-core star correlation obstruction.
9. The common-run point law and exact unrestricted memory-kernel trade
   equations.
10. The finite factor-atom identities under \(G_H+P_H\).
11. The even partial-collar formula (8.7), near-factor formula (8.15), and
   their product-SCD composition.
12. The odd collar, tail, and floor formulas (8.18)--(8.22), under the
   hypotheses specified in Section 7.

### Not proved

1. A nested/hash/SCD bank satisfying relative shore motion, the common run
   line, semigroup consistency, and integral memory circulation.
2. An abundance theorem for memory-kernel unlocking trades in the exact
   required fibre.
3. A compiler-safe central construction with full support or aggregate
   physical defect \(o(W)\) at \(H/\sqrt m\to\infty\), with the required
   cycle ledger.

Therefore the revised report's main conclusion is valid:

\[
\boxed{
\text{terminal exact multiplicity balancing is not a separate
coefficient-one gate once a legal literal central compiler exists.}}
\]

The surviving gate is the compiler-safe super-Gaussian central support
construction itself.
