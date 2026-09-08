# Fixed decorations, monotone kernels, and the stopped-variance baseline mismatch

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Verdict

Expanding all priority orders into literal fixed decorations is legitimate for
the current dynamic-quarantine priority nibble. After the one-time floor and
deadline parameters have been fixed, every operation in the live construction
only deletes fixed decorations. In particular, the live decorated catalogue is
a multihypergraph

\[
   \mathcal H_t\subseteq \mathcal H_0.                         \tag{0.1}
\]

Consequently all decorated codegrees and all fixed-conflict triple counts are
monotone. The following conditional implications are exact. If every relevant
unstopped fibre satisfies

\[
   d_t(v)\ge c_t d_0(v),                                       \tag{0.2}
\]

then normalized pair-square rows inflate by at most \(c_t^{-2}\), normalized
triangles inflate by at most \(c_t^{-3}\), and the exact priority common-link
second moment inflates by at most \(c_t^{-3}\).

The proposed closure nevertheless does **not** follow with the current
resource-density parameter. In the audited notation

\[
 z_t=\prod_{s<t}q_s,\qquad
 \rho_{1,s}=q_s^{g-1},                                         \tag{0.3}
\]

so even an ideal scalar degree theorem gives the one-root degree reference

\[
 a_t:=\prod_{s<t}\rho_{1,s}=z_t^{g-1},                         \tag{0.4}
\]

up to the already isolated cumulative mean error. It does not give
\(d_t(v)\ge (1-o(1))z_t d_0(v)\). At the stopping resource density
\(z_t=1/\log m\), with \(g=m^{1/2+o(1)}\),

\[
 \frac{a_t}{z_t}=z_t^{g-2}
 =\exp\!\left(-(1+o(1))g\log\log m\right)=o(1).                \tag{0.5}
\]

Thus monotonicity supplies only

\[
 a_t^{-2}=z_t^{-2(g-1)},\qquad a_t^{-3}=z_t^{-3(g-1)},         \tag{0.6}
\]

not the desired \(z_t^{-2}\) and \(z_t^{-3}\). These losses are sharp for
literal fixed-deletion systems, even when all protected degrees have exactly
the same contraction. Hence predictable **one-root** mean-spread alone cannot
close hereditary pair-square. The missing information remains contraction of
pair links at the scale \(z_t^{g-2}\), or an equivalent conditioned
common-link statement.

There is a useful conditional theorem: if one separately proves the much
stronger lower bound (0.2) with \(c_t=(1-o(1))z_t\), then fixed-decoration
monotonicity does close the total variance budget at

\[
 B_mW=m^{-1/2+o(1)}W,                                          \tag{0.7}
\]

and the global stopped Doob theorem applies. The issue is that this premise is
not the scalar degree theorem of the present nibble.

## 1. Audit of the literal fixed-decoration expansion

Fix a base grid \(P\), its phase set, and the already chosen integer deadline
parameters \(\bar d_q\). A priority decoration is a fixed permutation \(\pi\)
of the phases. At depth \(q\), the decoration claims the fixed suffix

\[
 C_q(\pi)=\{i:\operatorname{pos}_\pi(i)>\bar d_q\}.             \tag{1.1}
\]

The physical lower and upper targets attached to these phases are part of the
decoration. Owners, the full exposed grid, the tag, and all claimed targets are
therefore fixed data of \((P,\pi)\).

Suppose phase \(i\) has first unavailable depth \(r_t(i)\), with
\(r_t(i)=Q+1\) when it is unblocked. The fixed permutation \(\pi\) is feasible
at time \(t\) exactly when

\[
 \operatorname{pos}_\pi(i)\le \bar d_{r_t(i)}
 \quad\hbox{for every blocked phase }i.                         \tag{1.2}
\]

Equivalently, none of the fixed targets claimed by \((P,\pi)\) has already
been used. As time increases, used targets and used owners only accumulate,
and a first unavailable depth can only move to a more restrictive depth.
Thus (1.2) can change only from true to false. The factorial quantity
\(\Pi_t(P)\) is exactly the number of permutations \(\pi\) satisfying (1.2);
the usual factorial update is merely a quotient count of the fixed
permutations deleted between times \(t\) and \(t+1\).

This resolves the apparent adaptivity. Choosing a new legal priority for an
emitted base grid means choosing one currently surviving fixed copy
\((P,\pi)\). It does not change the claims of a previously fixed copy.

The remaining operations have the following literal interpretations.

1. Using a middle owner or a protected claimed target deletes every fixed
   decoration containing that resource.
2. Rejecting a tentative chunk in the alteration adds no edge and regenerates
   no deleted decoration.
3. The auxiliary wasteful restriction deletes fixed decorations conflicting
   with tentative choices, including rejected choices. It is again only
   deletion.
4. The \(s=4\) quarantine relation is a fixed relation between full base
   grids. Quarantining a neighbour deletes all its fixed priority copies.
5. The floor, cap, and enlarged deadline integers are fixed before
   \(\mathcal H_0\) is declared. Recomputing the number of feasible priorities
   does not change those integers.

Therefore (0.1) is valid, with multiplicities retained. A temporary
within-bite restriction may either be forgotten after the bite, in which case
it was never part of \(\mathcal H_t\), or retained as the stated wasteful
restriction, in which case it is another deletion.

There are operations used in other lanes which would not satisfy (0.1):
increasing \(\bar d_q\) after time zero, replacing one priority copy by a new
copy with different claims, or repairing a candidate by deleting phase columns
from that same candidate. None of these is an operation in the present
fixed-deadline nibble. If one is introduced later, its possible outputs must
first be expanded as fixed initial decorations; otherwise the argument below
does not apply.

## 2. Exact monotone normalized-kernel lemma

Let \(\mathcal H_0\) be a finite decorated multihypergraph and
\(\mathcal H_t\subseteq\mathcal H_0\). Write

\[
 d_t(x)=|\{e\in\mathcal H_t:x\in e\}|,
 \qquad
 d_t(x,y)=|\{e\in\mathcal H_t:x,y\in e\}|,                     \tag{2.1}
\]

with multiplicities. Put

\[
 K_t(x,y)=\frac{d_t(x,y)}{\sqrt{d_t(x)d_t(y)}}.                 \tag{2.2}
\]

Let \(G_t\) be a set of protected vertices such that

\[
 d_t(v)\ge c_vd_0(v)>0\qquad(v\in G_t).                        \tag{2.3}
\]

### Lemma 2.1 (termwise domination)

For \(x,y\in G_t\),

\[
 K_t(x,y)\le(c_xc_y)^{-1/2}K_0(x,y).                           \tag{2.4}
\]

Consequently, for every set \(B\) of vertices and every \(x\in G_t\),

\[
 \sum_{y\in B\cap G_t}K_t(x,y)^2
 \le
 \frac1{c_x\inf_{y\in B\cap G_t}c_y}
 \sum_{y\in B}K_0(x,y)^2.                                    \tag{2.5}
\]

Moreover,

\[
\begin{aligned}
 &\sum_{y,z\in G_t}K_t(x,y)K_t(y,z)K_t(z,x)\\
 &\quad\le
 \frac1{c_x}
 \sum_{y,z}
 \frac{K_0(x,y)K_0(y,z)K_0(z,x)}{c_yc_z}.                     \tag{2.6}
\end{aligned}
\]

In particular, if every displayed \(c_v\ge c\), then the losses in
(2.5) and (2.6) are at most \(c^{-2}\) and \(c^{-3}\), respectively.

#### Proof

Since \(\mathcal H_t\subseteq\mathcal H_0\),
\(d_t(x,y)\le d_0(x,y)\). Combining this with (2.3) proves (2.4).
Squaring and summing proves (2.5). Multiplying the three inequalities
(2.4) for \((x,y),(y,z),(z,x)\) cancels the square roots and gives the
factor \((c_xc_yc_z)^{-1}\); summing proves (2.6). \(\square\)

The same proof applies to typed exposed/claimed incidences by making a
separate vertex copy for every incidence type. Alternatively, the exact
priority common-link admits the following direct fixed-conflict proof.

## 3. Exact fixed-conflict domination of priority variance

Let \(\mathcal E_t(F)\) be the surviving fixed decorations in fibre \(F\),
and set \(D_t(F)=|\mathcal E_t(F)|\). Let \(R\) be any fixed conflict
relation between a tentative decoration \(e\) and a decoration \(f\) which
may be killed by it. It may include owner collision, exposed-to-claimed
target collision, and the fixed quarantine graph.

For a tentative tag \(U\), define

\[
 N_t(F,U)=
 \#\{(e,f_1,f_2):e\in\mathcal E_t(U),\ f_1,f_2\in\mathcal E_t(F),
                    \ eRf_1,\ eRf_2\}.                         \tag{3.1}
\]

If a live decoration at \(U\) is sampled uniformly, the exact squared
fractional loss of \(F\), summed over possible killer tags, is

\[
 J_t(F)=\sum_U\frac{N_t(F,U)}{D_t(F)^2D_t(U)}.                  \tag{3.2}
\]

Quotienting fixed priorities back to base grids turns the binary indicators
in (3.1) into the familiar fractional hazards; equation (3.2) is unchanged.

### Lemma 3.1 (fixed-conflict triple domination)

Suppose

\[
 D_t(F)\ge c_FD_0(F),\qquad D_t(U)\ge c_UD_0(U)                \tag{3.3}
\]

for every active killer tag \(U\). Then

\[
 J_t(F)
 \le
 c_F^{-2}\sum_Uc_U^{-1}
 \frac{N_0(F,U)}{D_0(F)^2D_0(U)}.                              \tag{3.4}
\]

In particular, if all relevant ratios are at least \(c\),

\[
 J_t(F)\le c^{-3}J_0(F).                                      \tag{3.5}
\]

#### Proof

Every triple counted by \(N_t(F,U)\) is a triple of fixed decorations
already counted by \(N_0(F,U)\), so \(N_t(F,U)\le N_0(F,U)\). Apply
(3.3) to the three denominator factors in each summand of (3.2). \(\square\)

Thus the formerly problematic cross-slice square is not a new object once
all decorations and the conflict relation are fixed: it is part of the
monotone numerator \(N_t\). The only possible amplification is through the
three fibre denominators. This observation is exact, but the denominator
scale is decisive.

The dynamic four-antichain quarantine does not spoil the statement. Its
relation is fixed. It may either be included in \(R\), or charged separately
by the deterministic quarantine ledger. For a raw fibre of size comparable
to \(A\), the maximum bad-neighbour degree is \(\xi_4A\), where
\(\xi_4=m^{-5+o(1)}\). Double counting bad pairs incident with one fibre gives
raw first moment at most \(O(\xi_4)\), and hence raw squared loss at most
\(O(\xi_4)\). This is negligible beside the raw
\(m^{-1+o(1)}\) common-link triangle. Equivalently, outside the already proved
\(o(W)\) exceptional ledger, cumulative quarantine deletion is at most
\(m^{-4}\) of the original fibre and may be charged deterministically.

## 4. The conditional stopped-variance theorem

This section records exactly what the proposed argument would prove if its
degree premise held at the resource-density scale.

Assume the following through a parallel bite process.

1. The raw weighted priority common-link budget over all protected fibres is

   \[
     \sum_F\operatorname{wt}(F)J_0(F)
     \le Qm^{-1+o(1)}W=m^{-1/2+o(1)}W.                         \tag{4.1}
   \]

   Here the target fibres have total accounting mass \(O(QW)\), the raw
   anchored common-link is \(m^{-1+o(1)}\), and the tag block is negligible.
2. The total effective activation time is \(m^{o(1)}\), in the present
   application \(O(\log\log m)\).
3. Before its stopping time and before direct consumption, every relevant
   fibre obeys

   \[
      D_t(F)\ge(1-\eta)z_tD_0(F),
      \qquad z_t\ge1/\log m.                                  \tag{4.2}
   \]

Reveal the independent tag coordinates of each parallel bite one at a time.
For a root \(x\), stop strictly before its direct-consumption time. Conditional
on \(x\) surviving the bite, the law at tag \(U\) has denominator

\[
  1-\alpha_t q_U(x)\ge1-\alpha_t.                              \tag{4.3}
\]

Thus, for \(\alpha_t\le1/2\), conditioning multiplies the one-coordinate
second moment by at most two. The inactive atom in the parallel law is
essential here. In a sure-active sequential law the denominator is
\(1-q_U(x)\), which need not be bounded below.

Lemma 3.1, (4.1), and (4.2) give total stopped predictable quadratic
variation

\[
\begin{aligned}
 \mathcal V
 &\le
 O(1)(1-\eta)^{-3}
   \left(\inf_tz_t\right)^{-3}
   m^{o(1)}
   \sum_F\operatorname{wt}(F)J_0(F)+o(W)\\
 &\le
 (\log m)^3m^{o(1)}m^{-1/2+o(1)}W+o(W)\\
 &=m^{-1/2+o(1)}W.                                             \tag{4.4}
\end{aligned}
\]

The terminal consuming increment is not included. If it were included,
consumed roots alone would contribute \(\Theta(W\sqrt m)\), so this lifetime
qualification is necessary.

Put \(B_m=m^{-1/2+o(1)}\) and \(\eta=B_m^{1/4}\). The weighted stopped Doob
argument then bounds the fibres exiting through martingale fluctuation by

\[
 O(B_m/\eta^2)W=O(B_m^{1/2})W=o(W),                            \tag{4.5}
\]

and the logarithmic square-remainder exit by

\[
 O(B_m/\eta)W=O(B_m^{3/4})W=o(W).                              \tag{4.6}
\]

If, in addition, the predictable log-losses have a common stratum reference,

\[
 \sup_t\left|
   \sum_{s<t}\left(\mathbb E[I_{s,F}\mid\mathcal F_s, F\text{ survives}]
                    -\mu_{s,r(F)}\right)
 \right|=o(1)                                                  \tag{4.7}
\]

outside another \(o(W)\) weighted family, then

\[
 D_t(F)=D_0(F)\exp\!\left(-\sum_{s<t}\mu_{s,r(F)}\right)
          (1+o(1))                                             \tag{4.8}
\]

uniformly. Equations (4.4)--(4.8) are a complete conditional
variance-plus-mean theorem.

## 5. Why the premise has the wrong scale in the current nibble

The current one-bite ideal exponents are

\[
 \rho_{1,t}=q_t^{g-1},\qquad \rho_{2,t}=q_t^{g-2}.             \tag{5.1}
\]

The first is the contraction of a one-root decorated degree; the second is
the contraction of a two-root link. Consequently, even with zero predictable
mean-spread and zero martingale error,

\[
 \frac{D_t(x)}{D_0(x)}
 =\prod_{s<t}\rho_{1,s}
 =z_t^{g-1},
 \qquad z_t=\prod_{s<t}q_s.                                   \tag{5.2}
\]

This exponent is also forced in the elementary product model: an edge through
a surviving root has \(g-1\) other independently retained coordinates, so its
survival probability is \(z_t^{g-1}\). One may make this deterministic by
taking a complete product catalogue with \(g-1\) coordinate classes and
retaining exactly a \(z_t\)-fraction of each class.

Therefore the stopped scalar theorem, even after (4.7) is proved, yields

\[
 D_t(F)\ge(1-o(1))z_t^{g-1}D_0(F),                             \tag{5.3}
\]

not (4.2). Applying Lemmas 2.1 and 3.1 with the actually available scalar
ratio gives

\[
 S_{t,h}(x)\le(1+o(1))z_t^{-2(g-1)}S_{0,h}(x),                 \tag{5.4}
\]

and

\[
 J_t(F)\le(1+o(1))z_t^{-3(g-1)}J_0(F).                        \tag{5.5}
\]

At \(z_t=1/\log m\), neither factor is \(m^{o(1)}\); rather,

\[
 z_t^{-3(g-1)}
 =\exp\!\left((3+o(1))g\log\log m\right).                    \tag{5.6}
\]

Thus (4.4) becomes useless. Renaming the degree reference
\(a_t=z_t^{g-1}\) as a new symbol \(z_t\) makes the formal statement
\(J_t\le z_t^{-3}J_0\) true, but does not repair the asymptotic accounting.

The desired cancellation uses both exponents in (5.1):

\[
 \frac{\rho_{2,t}^2}{\rho_{1,t}^2}=q_t^{-2}.                   \tag{5.7}
\]

Monotonicity discards \(\rho_{2,t}\) entirely. Hence a pair-link contraction
statement at scale \(q_t^{g-2}\), such as the conditioned mean-link condition
(CM), remains necessary.

## 6. Sharp fixed-deletion obstructions

The losses in Lemmas 2.1 and 3.1 cannot be improved using equal one-root
degrees, fixed decorations, or predictable mean-spread.

### Proposition 6.1 (sharp pair-square and triangle inflation)

Fix rational \(0<a<1\) and an integer \(D\) for which \(aD\) and
\(aD/2\) are integers.

For the pair-square example, take protected roots \(x,y\), \(aD\) fixed
edge copies containing both roots, and \((1-a)D\) additional copies through
each root separately. Initially

\[
 d_0(x)=d_0(y)=D,\qquad d_0(x,y)=aD.                           \tag{6.1}
\]

Delete all separate copies and retain the common copies. Then

\[
 d_t(x)=d_t(y)=aD,\qquad d_t(x,y)=aD,                          \tag{6.2}
\]

so

\[
 K_0(x,y)=a,\qquad K_t(x,y)=1.                                \tag{6.3}
\]

The squared normalized codegree inflates by exactly \(a^{-2}\).

For the triangle example, take protected roots \(x,y,z\). For each of the
three pairs create \(aD/2\) fixed copies containing that pair but not the
third root, and give each root \((1-a)D\) additional separate copies. Every
root initially has degree \(D\). Delete the separate copies. Every root now
has degree \(aD\), while each pair codegree remains \(aD/2\). Hence every
normalized pair entry changes from \(a/2\) to \(1/2\), and the off-diagonal
triangle anchored at any root inflates by exactly \(a^{-3}\).

Distinct copies may be made simple by adjoining private unprotected labels.
The process is literal deletion and all protected roots have exactly the same
degree ratio \(a\). \(\square\)

### Proposition 6.2 (sharp fixed-conflict common-link inflation)

Take fibres \(F,U\), each containing \(D\) fixed decorations. Mark a core of
size \(aD\) in each fibre, and let the fixed conflict relation be complete
between the two cores and empty elsewhere. Delete every noncore decoration.
Then both fibre degrees have ratio exactly \(a\). Initially, a uniformly
sampled decoration of \(U\) lies in its core with probability \(a\), and in
that case kills an \(a\)-fraction of \(F\). Therefore

\[
 J_0(F)=a\cdot a^2=a^3.                                       \tag{6.4}
\]

After deletion every surviving killer deletes all of the surviving fibre, so

\[
 J_t(F)=1=a^{-3}J_0(F).                                       \tag{6.5}
\]

Thus the cross-slice/common-owner square can attain the full denominator loss
even with perfect, equal, deterministic degree contraction. \(\square\)

Taking \(a=z_t^{g-1}\) in either proposition proves that fixed-decoration
deletion plus exact scalar mean-spread cannot yield the desired
\(z_t^{-2}\) pair-square or \(z_t^{-3}\) common-link bounds.

## 7. Exact surviving gate

The audit therefore separates two statements.

1. **Proved structural statement.** The priority/deadline/quarantine process
   is binary deletion of fixed decorations. Conditional on a lower degree
   ratio \(c_t\), pair-square and fixed-conflict common-link inflate by at
   most \(c_t^{-2}\) and \(c_t^{-3}\). Cross-slice physical-label quadratic
   variation is absorbed into the fixed triple numerator.
2. **Failed numerical identification.** The available scalar ratio is
   \(c_t\asymp z_t^{g-1}\), not \(z_t\). Therefore this structural theorem
   does not give the critical \(z_t^{-2}\) hereditary profile or the
   \(B_m=m^{-1/2+o(1)}\) variance budget.

The exact next statement is still a link-versus-degree theorem. In one-bite
form it must retain the cancellation

\[
 d_{t+1}(x,y)\approx q_t^{g-2}d_t(x,y),\qquad
 d_{t+1}(x)\approx q_t^{g-1}d_t(x),                             \tag{7.1}
\]

in the survival-conditioned weighted sense. Equivalently, one needs (CM)
and enough conditioned common-link control to justify its iteration. A proof
of scalar predictable mean-spread alone is insufficient.

No coefficient-one conclusion follows from fixed-decoration monotonicity.
