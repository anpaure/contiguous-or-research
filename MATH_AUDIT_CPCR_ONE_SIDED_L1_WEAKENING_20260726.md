# Audit of one-sided and \(L^1\) weakenings of CPCR

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

CPCR is substantially stronger than the exact constant-one transfer
needs.  It may be replaced by the summed missing-shadow condition itself,
or equivalently by either of the following exact one-sided functionals:

\[
 \boxed{
 \mathfrak H
   =\sum_{q\le H}\sum_{\epsilon\in\{-,+\}}\sum_T
        (1-L_q^\epsilon(T))_+
   =o(W),}                                          \tag{0.1}
\]

or

\[
 \boxed{
 \mathfrak X
 =\sum_{q,\epsilon}
   \left[
      \sum_T(L_q^\epsilon(T)-1)_+
        -(G-N_q)_+
   \right]
 =o(W),}                                           \tag{0.2}
\]

provided the already proved owner leave gives

\[
 \sum_{q,\epsilon}(N_q-G)_+=o(W).                  \tag{0.3}
\]

In the present packet theorem \(G=W-o(W/H)\), and in fact the leave is
exponentially small, so (0.3) holds.  For every protected \(q\ge1\),
eventually \(G>N_q\), and (0.2) simplifies to

\[
 \sum_{q,\epsilon}
 \left[
   \sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)
 \right]=o(W).                                     \tag{0.4}
\]

Equation (0.1) is the weakest exact separable load functional: for
nonnegative integer loads,

\[
                         (1-L)_+=\mathbf1_{\{L=0\}}.
\]

It ignores every positive multiplicity, however large, and still implies
the constant-one OR transfer because the transfer only appends missing
masks.

There is an important qualification.  Heavy overloads may be ignored
only when holes are controlled **directly** by (0.1).  If one uses mass
conservation and an upper-repeat surrogate such as (0.2), every overload
unit must be counted linearly.  Capping or deleting the heavy tail is
invalid: one target of load \(\Theta(W)\) can pay for \(\Theta(W)\)
missing targets.

The weakening is not equivalent to MWB.  MWB controls distance to a
balanced floor/ceiling load vector, including positive underloads and
excessive multiplicities.  Perfect target coverage can coexist with
\(\Theta(W)\) MWB defect.  Conversely MWB can hold while CPCR fails
because CPCR squares a sublinear but concentrated overload spike.

The exact hierarchy is therefore

\[
 \text{CPCR}\Longrightarrow\text{MWB}
 \Longrightarrow\text{missing shadows}
 \Longrightarrow\text{constant-one transfer},     \tag{0.5}
\]

with neither converse valid in general.  For the final transfer, the
right irreducible statement is (0.1), not CPCR and not MWB.

## 1. Exact load ledger

Fix a signed depth \(c=(q,\epsilon)\).  There are \(N_q\) available
targets and exactly \(G\) retained packet occurrences.  Write

\[
                         L_c(T)\in\mathbb Z_{\ge0},
 \qquad
                         \sum_TL_c(T)=G.             \tag{1.1}
\]

Define

\[
 M_c=\#\{T:L_c(T)=0\},\qquad
 E_c=\sum_T(L_c(T)-1)_+.                            \tag{1.2}
\]

If \(U_c=\{T:L_c(T)>0\}\), then

\[
 E_c
 =\sum_{T\in U_c}(L_c(T)-1)
 =G-|U_c|,
\]

while

\[
                         M_c=N_q-|U_c|.
\]

Hence

\[
 \boxed{M_c=N_q-G+E_c.}                            \tag{1.3}
\]

This is the exact missing/repeat identity.  It contains no moment
estimate and no balanced-quota approximation.

Put

\[
 F_c=(N_q-G)_+,\qquad
 X_c=E_c-(G-N_q)_+.                                \tag{1.4}
\]

Equation (1.3) gives the nonnegative decomposition

\[
 \boxed{M_c=F_c+X_c.}                              \tag{1.5}
\]

Thus \(F_c\) is the forced cardinality deficit and \(X_c\) is the repeat
mass above its unavoidable baseline.

For the packet theorem,

\[
                         W-G=o(W/H).
\]

Since \(N_q\le W\),

\[
 \sum_{q\le H,\epsilon}F_c
 \le2H(W-G)=o(W).                                  \tag{1.6}
\]

Summing (1.5) proves the equivalence of (0.1) and (0.2).

## 2. Weakest direct one-sided functional

Since \(L_c(T)\) is a nonnegative integer,

\[
                         (1-L_c(T))_+
 =\begin{cases}
 1,&L_c(T)=0,\\
 0,&L_c(T)\ge1.
 \end{cases}                                       \tag{2.1}
\]

Therefore

\[
 \boxed{
 \sum_{c,T}(1-L_c(T))_+=\sum_cM_c.}                \tag{2.2}
\]

This is both necessary and sufficient for the physical missing-shadow
conclusion.  It is an \(L^1\) lower hinge at the only threshold relevant
to coverage.

Among nonnegative separable load penalties which vanish on every covered
coordinate, it is the literal indicator cost of an uncovered coordinate.
No positive load needs to be distinguished from any other positive load
for the OR transfer.

## 3. Constant-one transfer from the one-sided criterion

The diverse packet theorem supplies:

1. \(G=W-o(W/H)\) retained middle owners;
2. \(G/(2R)=o(W/H)\) cyclic components;
3. literal lower and upper targets through every \(q\le H\); and
4. the exterior product-SCD tail of length \(o(W)\).

Linearize every cyclic component using the audited repeated-prefix
interface, at total cost \(o(W)\).  Append every omitted middle owner and
every missing signed band target once.  The resulting length is

\[
 \begin{aligned}
 &G+(W-G)+o(W)
   +\sum_{q\le H,\epsilon}M_q^\epsilon\\
 &\hspace{35mm}=W+o(W)
 \end{aligned}                                     \tag{3.1}
\]

under (0.1).  Cross-block windows only add masks.  Appending the exterior
tail proves the exact constant-one upper bound.

Thus CPCR's upper-tail and quadratic information is not consumed anywhere
in the transfer.

## 4. A quota-deficit sufficient condition

Let

\[
 c_q=\left\lfloor{G\over N_q}\right\rfloor\ge1
\]

and define the lower quota deficit

\[
                         D_c^-=\sum_T(c_q-L_c(T))_+.             \tag{4.1}
\]

Every hole contributes exactly \(c_q\), so

\[
                         M_c\le {D_c^-\over c_q}.   \tag{4.2}
\]

Consequently

\[
 \boxed{
 \sum_c{D_c^-\over c_q}=o(W)}                      \tag{4.3}
\]

is another one-sided sufficient theorem.

It is not the weakest theorem and is not equivalent to coverage.  For
example, take \(G=2N\), \(c=2\), and let half the loads equal \(1\) and
half equal \(3\).  Then

\[
                         M=0,\qquad D^-={N\over2}.  \tag{4.4}
\]

Coverage is perfect while (4.3) has linear cost.

At quota \(c_q=1\), (4.1) reduces exactly to the missing count.  At larger
quotas it additionally penalizes positive but under-quota targets, which
the OR transfer does not care about.

## 5. Relation to MWB

For one typed depth, write

\[
 \begin{aligned}
 D_c^-&=\sum_T(c_q-L_c(T))_+,\\
 D_c^+&=\sum_T(L_c(T)-c_q-1)_+.
 \end{aligned}                                     \tag{5.1}
\]

The exact balanced-quota overload is

\[
                         O_c=\max\{D_c^-,D_c^+\}.   \tag{5.2}
\]

MWB asks for an aggregate condition of the form

\[
                         \sum_c{O_c\over c_q}=o(W). \tag{5.3}
\]

By (4.2), MWB implies missing-shadow control.  The converse fails even
with no holes.

### Counterexample 5.1 (coverage does not imply MWB)

Let \(N\) be even, \(G=2N\), and \(c=2\).  Give \(N/2\) targets load
\(1\) and \(N/2\) targets load \(3\).  Then every target is covered, but

\[
 D^-={N\over2},\qquad D^+=0,\qquad
 {O\over c}={N\over4}.                             \tag{5.4}
\]

Thus the exact transfer defect is zero while the MWB defect is linear.

This example also shows why calling a threshold-\(c_q\) lower-tail
functional “equivalent to MWB” is incorrect.

## 6. Relation to CPCR

CPCR uses

\[
 \Phi_c
 =\sum_T
   (L_c(T)-c_q)(L_c(T)-c_q-1).                     \tag{6.1}
\]

For integer \(z\),

\[
 (z-c)(z-c-1)
 \ge2(c-z)_++2(z-c-1)_+.                           \tag{6.2}
\]

Hence

\[
                         2O_c
 \le2(D_c^-+D_c^+)
 \le\Phi_c.                                        \tag{6.3}
\]

After summation, CPCR implies MWB and therefore (0.1).

The converse fails because CPCR charges overloads quadratically.

### Counterexample 6.1 (MWB does not imply CPCR)

Take \(G=N\), \(c=1\), and put

\[
 k=\lfloor\sqrt N\rfloor.
\]

Assign:

* load \(0\) to \(k\) targets;
* load \(k+1\) to one target; and
* load \(1\) to the remaining \(N-k-1\) targets.

The total load is \(N\).  Moreover

\[
 D^-=k,\qquad D^+=k-1,\qquad O=k=o(N).             \tag{6.4}
\]

Thus MWB and the missing-shadow condition both hold at this scale.  But

\[
 \Phi
 =2k+k(k-1)
 =\Theta(N),                                       \tag{6.5}
\]

so CPCR fails.

This is precisely a heavy-overload example which is harmless for
constant-one coverage and for linear MWB, but fatal to quadratic CPCR.

## 7. Heavy overload tails: what may and may not be ignored

### Safe statement

When (0.1) is verified directly, every load \(L\ge1\) has zero cost.
The complete upper tail may be ignored, including isolated loads of
arbitrarily large multiplicity.

### Unsafe statement

If holes are inferred from the repeat identity (1.3), overload
multiplicity is the mass which pays for the holes and cannot be capped.

Fix \(0<\alpha<1\), put \(k=\lfloor\alpha N\rfloor\), take
\(G=N\), and assign:

* load \(0\) to \(k\) targets;
* load \(k+1\) to one target; and
* load \(1\) to all remaining targets.

Then

\[
                         M=k,\qquad E=k.            \tag{7.1}
\]

For a capped repeat functional

\[
 E_B=\sum_T\min\{(L(T)-1)_+,B\},                   \tag{7.2}
\]

one has

\[
                         E_B=B.                    \tag{7.3}
\]

Choosing \(B=o(N)\) makes the capped functional \(o(W)\) while
\(M=\Theta(W)\).  Counting only the number of overloaded targets is even
worse: it gives one.

More generally, any upper-tail charge \(\tau(k)=o(k)\) can miss a linear
hole count concentrated behind one load-\(k+1\) target.  Thus the exact
linear excess in (0.2) is the weakest safe repeat-based functional.

## 8. Exact conclusion

The proposed weakening is valid in the following precise form.

### Minimal missing-shadow form

It is enough—and at the physical load level exactly equivalent—to prove

\[
 \boxed{
 \sum_{q\le H,\epsilon,T}(1-L_q^\epsilon(T))_+=o(W).}
\]

This ignores every overload tail.

### Equivalent repeat-excess form

It is equally enough to prove

\[
 \boxed{
 \sum_{q,\epsilon}
 \left[
   \sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)_+
 \right]=o(W),}
\]

together with the already available forced-deficit estimate (0.3).
This formulation must retain full linear overload mass.

### Stronger sufficient lower-quota form

The condition

\[
 \boxed{
 \sum_{q,\epsilon}{1\over c_q}
   \sum_T(c_q-L_q^\epsilon(T))_+=o(W)}
\]

is sufficient but not equivalent.

None of these one-sided statements is equivalent to MWB, and MWB is not
equivalent to CPCR.  CPCR remains a convenient quadratic sufficient
target for covariance methods, not the exact theorem consumed by the
constant-one transfer.

## 9. Cross-parent grouped-Hall refinement

MATH_THEOREM_L1_RECAST_CROSS_PROFILE_PACKET_UNION_AND_GROUPED_HALL_20260726.md
recasts the earlier mixed-profile and frozen-parent cuts directly for
\(\mathfrak H\) and \(\mathfrak X\). They give linear defects only in
their fixed incidence spaces; legal cross-parent slab trades can repair
them at a dense but permitted slab scale.

For any owner-disjoint compound choice-group catalogue, the successor
note proves that the minimum integral missing mass equals the minimum
product avoidance functional

\[
 \sum_{c,T}\prod_g(1-p_{g,c}(T)).
\]

It also gives a tensorable two-group counterexample in which every natural
grouped rank Hall inequality and every mean-one marginal holds, while
every state has one hole and one repeat per four targets. Thus the exact
weaker residual is grouped all-depth near-cover or homing, not a
first-moment Hall theorem and not covariance.
