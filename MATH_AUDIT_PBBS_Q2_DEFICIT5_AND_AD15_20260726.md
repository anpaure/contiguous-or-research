# Audit of the PBBS deficit-five \(q=2\) criterion and AD15 correction

Date: 2026-07-26  
Method: pure mathematics only; no computation or search

Audited reports:

* `PBBS_Q2_DEFICIT5_CRITERION_20260725.md`;
* the \(q=2\) portion of
  `MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md`.

## 0. Verdict

The combined theorem package is correct, with the following exact scope.

For every \(m\ge2\), every
\(S\in\binom{[2m+1]}{m-2}\), and the canonical PBBS factor,

\[
 \boxed{1\le\mu_{P,2}(S)\le10.}
\]

Here \(\mu_{P,2}(S)\) counts all oriented step-two starting states of the
factor, one for each rank-\(m\) state, not starts in one arbitrarily chosen
\(g=f^2\) orbit. Equivalently, one sums over all \(g\)-orbits and takes
indices modulo each orbit length.

The standalone deficit-five report has two proof omissions:

1. a two-edge path in its partial-permutation graph could superficially
   retain the same extra label on both edges; the pointwise no-gap-three
   theorem excludes this;
2. in the selected ten-mark boundary, the nonlocal equalities \(a=c\) and
   \(d=b\) require an explicit shared-coordinate cyclic-order argument.

AD15 states and correctly proves both missing points. Thus the theorem is
valid when the two reports are read together; the short proof in the
deficit-five report alone is incomplete at those two sentences.

The exact floor-one range is \(m\ge8\). Hence the overload and corrected
collision bounds in AD15 hold with their stated floor-one meaning for every
\(m\ge8\), not merely for an unspecified sufficiently large \(m\).

Finally, the cap ten is sharp under the theorem's quantifiers. At \(m=2\)
there is only one rank-zero target, \(S=\varnothing\). The no-gap-three
theorem makes every one of the
\(W=\binom52=10\) oriented starting states have intersection
\(\varnothing\). Therefore

\[
 \boxed{\mu_{P,2}(\varnothing)=10\quad(m=2).}
\]

No uniform cap below ten can replace the audited bound. A smaller cap after
adding the extra restriction \(m\ge8\) is not proved by the deficit-five
data and remains a separate question.

## 1. Exact definition and five-mark data

Let

\[
 n=2m+1,
 \qquad f:\binom{[n]}m\to\binom{[n]}m,
 \qquad g=f^2.
\]

Choose one representative notation \(A_i=f^i(A_0)\) on every oriented
\(f\)-component. The exact global multiplicity is

\[
 \mu_{P,2}(S)
 =\#\left\{A\in\binom{[n]}m:
 A\cap gA\cap g^2A=S\right\}.
 \tag{1.1}
\]

This is the unambiguous version of the indexed formula

\[
 \#\{i:A_i\cap A_{i+2}\cap A_{i+4}=S\}.
\]

In particular,

\[
 \sum_S\mu_{P,2}(S)=\binom{2m+1}m=W,
 \tag{1.2}
\]

because the pointwise no-gap-three theorem gives a unique rank-\((m-2)\)
color to every oriented start.

Fix \(S\) and put \(Z=[n]\setminus S\). Then

\[
 |Z|=m+3,
 \qquad n-2|S|=5.
\]

Hence the cyclic word of \(S\) has exactly five forward-unmatched and five
reverse-unmatched zeros. For \(u\in Z\), the core

\[
 C_u=S\cup\{u\}
\]

has deficit three. If \(p_u\) is the strict predecessor of \(u\) in the
five-element forward list and \(q_u\) is the strict successor in the
five-element reverse list, the one-flip deletion rule gives exactly

\[
 U_+(C_u)=\{p_u,\operatorname{pred}p_u,
                   \operatorname{pred}^2p_u\},
 \tag{1.3}
\]

\[
 U_-(C_u)=\{q_u,\operatorname{succ}q_u,
                   \operatorname{succ}^2q_u\}.
 \tag{1.4}
\]

These formulas cover both cases \(u\in U_\pm(S)\) and
\(u\notin U_\pm(S)\). At a coordinate shared by the forward and reverse
lists, the expanded physical order must be \(C_u,A_u\); AD15 retains this
order throughout.

## 2. Internal edges and exact support formula

For distinct \(a,u,c\in Z\), define

\[
 (a,u,c)\in\mathcal E_S
\]

by

\[
 c=\operatorname{pv}_{U_+(C_u)}(a),
 \qquad
 a=\operatorname{nx}_{U_-(C_u)}(c).
 \tag{2.1}
\]

The deficit-three predecessor/successor law gives the literal equivalence

\[
 g(S\cup\{a,u\})=S\cup\{u,c\}
 \quad\Longleftrightarrow\quad
 (a,u,c)\in\mathcal E_S.
 \tag{2.2}
\]

Thus the graph \(H_S\) on \(\binom Z2\), with arcs

\[
 \{a,u\}\longrightarrow\{u,c\},
\]

is exactly the subgraph of the PBBS permutation induced on states
containing \(S\). It has maximum indegree and outdegree one.

For an ordered central pair \((b,c)\), let
\(\operatorname{In}_S(b,c)\) and
\(\operatorname{Out}_S(b,c)\) be the two explicit indicators in the source
report. Since \(H_S\) is a partial permutation, their witnesses \(a,d\)
are unique.

The point requiring AD15 is the orientation of the second edge. Suppose

\[
 S\cup\{a,b\}\to S\cup\{b,c\}
\]

is followed by an edge which retains \(b\). Then all three states contain
\(S\cup\{b\}\), so their intersection has rank at least \(m-1\). This
contradicts the pointwise no-gap-three rank \(m-2\). Therefore the second
edge must retain \(c\), and every two-edge path contributing color \(S\)
has the unique orientation

\[
 S\cup\{a,b\}\to
 S\cup\{b,c\}\to
 S\cup\{c,d\}.
 \tag{2.3}
\]

Consequently the exact formula is

\[
 \boxed{
 \mu_{P,2}(S)=
 \sum_{\substack{b,c\in Z\\b\ne c}}
 \operatorname{In}_S(b,c)\operatorname{Out}_S(b,c).}
 \tag{2.4}
\]

There is no double count from reversing \((b,c)\): the unique incoming arc
in (2.3) retains \(b\), while the unique outgoing arc retains \(c\).
Equation (2.4) is therefore also equivalent to saying that \(S\) is
missing exactly when \(H_S\) has no directed two-edge path.

## 3. Complete support and all shared-mark cases

Expand the five forward marks \(A_x\) and five reverse marks \(C_x\) in
physical circular order, placing \(C_x,A_x\) consecutively at a shared
coordinate. Write the resulting ten-symbol word as

\[
 A^{\alpha_0}C^{\gamma_0}\cdots
 A^{\alpha_{t-1}}C^{\gamma_{t-1}},
 \qquad
 \sum_i\alpha_i=\sum_i\gamma_i=5.
\]

At the boundary after the \(i\)-th \(A\)-run, the two relevant gap counts
are exactly

\[
 x_i=
 \begin{cases}
 0,&\gamma_i\ge2,\\
 \alpha_{i+1},&\gamma_i=1,
 \end{cases}
 \qquad
 y_i=
 \begin{cases}
 0,&\alpha_i\ge2,\\
 \gamma_{i-1},&\alpha_i=1.
 \end{cases}
 \tag{3.1}
\]

The source's run selection is exhaustive:

* \(t=1\) is immediate;
* for \(t=2\), choose an \(A\)-run of size at least three;
* for \(t\ge3\), choose a largest \(A\)-run; if its size is at least two,
  the next \(A\)-run has size at most two, while if all sizes are one then
  \(t=5\) and every \(C\)-run also has size one.

Thus some boundary \(A_c,C_b\) has \(x_i,y_i\le2\). Let \(C_a\) be the
next reverse mark after \(C_b\), and let \(A_d\) be the preceding forward
mark before \(A_c\). Formulas (1.3)--(1.4) then give the two arrows (2.3).

The local inequalities alone do not state every required distinctness, but
AD15's cyclic-order repair is exact:

* \(a\ne b\), \(b\ne c\), and \(c\ne d\) follow from strict
  next/previous and from the local order \(C_x,A_x\);
* if \(a=c\), then the shared mark \(C_c\) occurs immediately before
  \(A_c,C_b\), while it is also required to be the next \(C\)-mark after
  \(C_b\). A five-element cyclic \(C\)-order cannot have one mark as both
  predecessor and successor of \(C_b\);
* the reverse five-element \(A\)-order excludes \(d=b\).

These are exactly the nonlocal equalities whose failure would make one of
the two swaps degenerate. The equality \(a=d\) is harmless and is not
excluded or needed. Hence the constructed two-edge path is valid for every
\(m\ge2\) and every \(S\), proving complete support.

## 4. Multiplicity cap and sharpness

For any occurrence (2.3), the first edge gives

\[
 a\in U_-(C_b)\subseteq U_-(S),
\]

and the second gives

\[
 b\in U_-(C_c)\subseteq U_-(S).
\]

The labels \(a,b\) are distinct. Their unordered pair is exactly the pair
of extras in the initial state \(S\cup\{a,b\}\). Since \(g\) is
deterministic, that initial state determines the whole oriented path.
Therefore

\[
 \mu_{P,2}(S)\le
 \binom{|U_-(S)|}{2}=\binom52=10.
 \tag{4.1}
\]

This injection has all quantifiers required by (1.1); no orbit-length or
choice-of-core multiplicity remains.

The bound is sharp. When \(m=2\), the target rank is zero, so the only
target is \(S=\varnothing\). There are \(W=\binom52=10\) oriented starts.
The pointwise rank theorem assigns a rank-zero intersection to each, and
that intersection must be \(\varnothing\). Hence

\[
 \mu_{P,2}(\varnothing)=10.
\]

Thus no theorem retaining the stated quantifier \(m\ge2\) can sharpen the
constant. The argument does not decide whether a smaller cap happens to
hold uniformly after imposing \(m\ge8\); neither audited report proves such
a restriction.

## 5. Floor and Catalan accounting

The average load denominator satisfies

\[
 {W\over\binom{2m+1}{m-2}}
 ={(m+2)(m+3)\over m(m-1)}.
\]

It lies in \([1,2)\) exactly for \(m\ge8\). Therefore, in precisely that
range, the balanced floor is one and

\[
 R_2=W-\binom{2m+1}{m-2}.
\]

Complete support and (1.2) give

\[
 \sum_S(\mu_{P,2}(S)-1)=R_2.
\]

For the AD15 definitions of balanced overload and corrected collision
energy,

\[
 O_2(P_m)\le R_2,
 \qquad
 Q_2(P_m)=\sum_S\binom{\mu_{P,2}(S)-1}{2}
          \le4R_2,
\]

because \(1\le\mu_{P,2}(S)\le10\). Finally,

\[
 {R_2\over\operatorname {Cat}_m}
 ={6(2m+1)(m+1)\over(m+2)(m+3)}<12,
\]

so

\[
 \boxed{O_2(P_m)<12\operatorname {Cat}_m,
 \qquad Q_2(P_m)<48\operatorname {Cat}_m}
 \qquad(m\ge8).
\]

All quantifiers, floors, and constants in the AD15 \(q=2\) conclusion are
therefore correct.

