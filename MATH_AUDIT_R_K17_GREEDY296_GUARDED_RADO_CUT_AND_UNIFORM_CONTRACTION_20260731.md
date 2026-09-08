# Independent audit: K17 greedy296 guarded Rado cut and uniform contraction

Date: 2026-07-31  
Audited file:
`MATH_THEOREM_R_K17_GREEDY296_GUARDED_RADO_CUT_AND_UNIFORM_CONTRACTION_20260731.md`  
Method: independent artifact arithmetic and symbolic proof audit; no SAT,
remote search, or bounded-radius enumeration.

## 0. Verdict

**VALID WITH THE STATED SCOPE.**

The decisive K17 claim is an exact obstruction to the complete fixed-base
pure residual-\(U\) fibre, not to all occurrence-changing or nonflat K17
repairs.  Its candidate neighborhood is empty before any matroid assumption
is used, so the rank-zero conclusion is robust.

The Rado and weighted-contraction formulas are correct for a complete
unit-debt serialization by closed compounds.  They are not valid if raw
exchange columns, branching packets, or packets from different occurrence
bases are treated as independent representatives.

The all-\(k\) conclusion is conditional.  It requires exact hard replay,
literal-weighted carried debt, bounded physical excess, protected deeper
witnesses, and regeneration of the same bounded interface.  It is not a
claim that the present K17 catalogue satisfies \(\rho<1\).

## 1. Artifact and arithmetic audit

The SHA-256 values in the theorem were recomputed locally:

\[
\begin{array}{c|c}
\text{file}&\text{SHA-256}\\ \hline
\texttt{k17\_opt28\_occurrence\_greedy296\_verified...flow.json}&
079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f\\
\texttt{k17\_opt28\_occurrence\_greedy296\_connected\_bflow\_v2...json}&
63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0\\
\texttt{h2\_k17\_opt28\_occurrence\_greedy296...audit.json}&
047bb2999a8ad22ad421740cd675bae49af64d52b9c80f2578a2d4db7366d433\\
\texttt{k17\_occurrence\_c6\_base\_fibre...audit.json}&
d556c41ebf4b6e33a122e101a45c050049b5f223efda3cd49b14d2edf03fece9.
\end{array}
\]

The replay JSON records exactly 296 component-interior signatures in 157
components, formal replay weight 478, and 177 arbitrary-residual zero-support
rank-ten targets.  Therefore

\[
                       296+177=473,
\qquad                 478+177=655.                       \tag{1.1}
\]

The second number is only a declared hard-defect weight.  The audit rejects
the stronger phrase "655 appendable masks": no casualty-set theorem turns
the run weights into distinct terminal masks.

For the donor imbalance profile,

\[
1848+210+2014+115+8=4195,
\]

and

\[
1848+2(210)+2014+2(115)+3(8)=4536.
\]

Its signed sum is

\[
-1848-2(210)+2014+2(115)+3(8)=0,
\]

as a degree divergence must be globally.  Thus the stated 4,195-owner,
\(L_1=4536\), max-3 imbalance is internally consistent.

## 2. Base--fibre audit

Subtracting the before/after degree identity

\[
                         d_M+d_F+d_R=2\mathbf1
\]

with \(F\) fixed gives \(\Delta d_R=-\Delta d_M\).  A residual alternating
circuit has zero boundary at each visited port, hence \(\Delta d_R=0\).
Therefore a base-changing occurrence move cannot be represented as an
independent residual fibre move.

The factorization audit reports 765 macro deletions and insertions, 710
changed ports with \(L_1=744\), and 4,674 changed residual pairs.  It also
reports exactly 710 bad ports if the old residual lift is combined with the
new base and zero bad ports for the matched old/old and new/new pairs.

**Verdict: valid.**  This independently rules out transplanting a circuit
catalogue from the old base without rebasing and replay.

## 3. Empty-neighborhood cut audit

There are two logically independent invariants.

1. A pure residual-\(U\) circuit changes residual incidences and not the
   ordered interior of a fixed macro.  Hence an interior zero-bracketed run
   signature is fixed under one circuit and, inductively, under every finite
   compound.
2. The 177 target set was obtained in a relaxation allowing every locally
   admissible residual port incidence, while dropping simultaneous balance
   and connectivity.  Every actual pure residual circuit state is a
   subfamily of this relaxation.  Zero support in the relaxation therefore
   implies zero support in every actual state.

Thus every candidate set for all 473 displayed obligations is empty.  The
union is empty and has rank zero in every matroid.  The Rado inequality for
that set reads \(0\ge473\) and fails.

**Verdict: valid and independent of circuit radius.**  No completeness
assumption about a finite C6 generator list is needed: the support
relaxation and macro-interior invariance cover arbitrary pure residual
pairings/circuits.

**Scope:** occurrence-changing, macro-interior, marked-bank-changing, and
genuinely nonflat packets are outside this cut.  The theorem does not claim
a global K17 obstruction.

## 4. Rado formula audit

For any \(Y\subseteq Q\), an independently represented subset of \(Q\) has
at most \(|Q\setminus Y|\) obligations outside \(Y\) and at most
\(r_M(A(Y))\) inside.  This gives

\[
r_N(Q)\le |Q\setminus Y|+r_M(A(Y)).
\]

Rado's independent-transversal theorem gives equality after minimizing
over \(Y\).  Taking \(Q=H\) yields the stated all-subsets hard Hall/rank
criterion.  In a strict gammoid, Menger's theorem converts the rank into a
minimum vertex/resource separator, provided the directed representation is
splice-closed and genuinely represents only legal packets.

**Verdict: valid.**

The warning about raw columns is necessary.  Degree-balanced selections are
not hereditary, so the 545,721 single-colour columns do not themselves form
a valid matroid ground of factor-feasible packets.

## 5. Weighted formula audit

Assume \(H\) is independent.  By the contraction identity,

\[
r_{N/H}(T)=r_N(H\cup T)-r_N(H)
          =r_N(H\cup T)-|H|.
\]

For a nonnegative integer-weighted matroid, greedy gives

\[
\max_{I\text{ independent}}w(I)
 =\sum_{t\ge1}r(\{o:w(o)\ge t\}).
\]

Applying this to \(N/H\) proves the service formula.  Subtracting from the
total additive weight proves the leave formula.

**Verdict: valid for additive declared tokens.**  If two unresolved tokens
would be repaired by appending the same literal mask, the formula is exact
for the token potential, not for the number of distinct appended masks.
Unitizing the common literal or retaining a conservative upper bound fixes
the interpretation.

## 6. Cost-to-go audit

The Bellman equation follows by splitting an accepting route after its
first arc.  Nonnegative costs prevent a negative-cycle pathology.  Tying
the minimum cost by minimum remaining hop count forces strict
lexicographic descent even over a zero-cost arc.  If no accepting route
exists, reachability or sublevel reachability supplies the corresponding
directed cut.

**Verdict: valid.**  This is the correct exact object when compounds branch
or when guard compatibility is not matroidal.  A failed Rado cut then
excludes only the declared serializable subatlas, whereas a full-state cut
excludes every represented physical route.

## 7. Uniform contraction algebra

From service \(R\) and new casualties \(C\le\theta R+b_1\),

\[
\Phi'\le\widehat\Phi-R+C
       \le\widehat\Phi-(1-\theta)R+b_1.
\]

Using \(R\ge\eta\widehat\Phi-\delta\) gives

\[
\Phi'\le[1-(1-\theta)\eta]\widehat\Phi
          +(1-\theta)\delta+b_1.
\]

Substitution of \(\widehat\Phi\le\lambda\Phi+b_0\) yields

\[
\rho=\lambda[1-(1-\theta)\eta],
\quad
B_0=[1-(1-\theta)\eta]b_0+(1-\theta)\delta+b_1.
\]

The fixed-point bound \(B_0/(1-\rho)\) is correct for \(\rho<1\).

**Verdict: valid.**  The theorem correctly requires a uniformly bounded
final physical excess, not an additive positive overhead accumulated at
every induction level.  It also correctly keeps exported palette/owner
debt in \(\Phi\), while allowing bounded terminal middle masks and terminal
common-cap omissions to be paid once.

## 8. Final proved boundary

The audit supports exactly these conclusions:

* a complete, unbounded-support pure-fibre K17 obstruction of rank deficit
  at least 473;
* no obstruction yet for occurrence-changing closed compounds;
* marginal rank-ten donor Hall passes, but balanced closure is unproved;
* a correct exact Rado/min-cost test once a complete closed packet gammoid
  is supplied;
* a correct conditional \(\rho<1\) theorem for \(B(k)+O(1)\).

It rejects the following stronger inferences:

* that 655 is already a distinct-literal append lower bound;
* that the old 5,433-hex catalogue can be attached to greedy296;
* that raw provider columns are matroid representatives;
* that one K17 rank certificate proves dimension-uniform regeneration; or
* that the current data prove \(\nu(17)=B(17)\) or an unconditional
  \(B(k)+O(1)\) theorem.
