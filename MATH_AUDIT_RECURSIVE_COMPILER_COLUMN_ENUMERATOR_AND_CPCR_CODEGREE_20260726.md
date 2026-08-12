# Recursive compiler column enumerator, post-antipode codegrees, and the CPCR boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Verdict

Write the physical compiler dimension as

\[
                         R=2n,\qquad n=4\cdot2^t,
\]

and put \(K=2^R\).  The binary parity recursion gives an exact finite-state
transfer formula for the complete pair enumerator

\[
                         A_{q,\epsilon}(a,\delta).
\]

The formula is Theorem 2.1 below.  It is uniform for every
\(q\le A\sqrt m\), because at the chosen packet scale \(q=o(n)\), and hence
every bottom \(Q_4\)-leaf receives at most two physical edges.  The same
transfer formula, with vector-valued column symbols, computes the common
all-depth, two-sign column catalogue under one affine label.

The calculation reveals a previously omitted large pair atom.  A short
physical window visits only

\[
 d_0(q)=\lceil q/2\rceil,\qquad
 d_1(q)=\lfloor q/2\rfloor+1
\]

bottom \(Q_4\)-leaves, according as it starts at a pair boundary or pair
midpoint.  Changing any two context bits in the unvisited leaves changes
two fixed physical \(b\)-columns but changes no direction in the window.
Consequently

\[
 \boxed{
 {A_q(q,2)\over K\binom{R-q}{2}}
 \ge {1\over2\binom{R-q}{2}}
 \left\{
  \binom{n-4d_0(q)}2+\binom{n-4d_1(q)}2
 \right\}
 ={1\over4}-o(1).}
\]

This survives contraction of the forced antipodal pairs.  If \(D_q\) is
the degree of a contracted face-supervertex in the full affine option
catalogue, then

\[
                         \Delta_2\ge(1/4-o(1))D_q.
\]

Thus antipodal fusion does **not** produce a locally low-codegree
hypergraph.  In particular, the proposed criterion
\(\Delta_2=o(D_q/K)\) is false by an exponential factor.

The dispersed selector does dilute this atom between physical packets.
Inside a dimension-\(S\) product cell, its packet-relative contribution is

\[
 (1+o(1))
 {\binom{R-q}{2}\over\binom{S-q}{2}}
 {A_q(q,2)\over K\binom{R-q}{2}}
 \ge(1/4-o(1))(R/S)^2.
\]

Since \(R=o(S)\), this is \(o(1)\) on the ordinary degree scale, but it is
still much larger than \(1/K\).  More importantly, the selector theorem
proves this as a packet-relative/annealed census, not as the quenched
cross-parent maximum-codegree or weighted Hall estimate needed by CPCR.

Accordingly there is no certified global type-count deficit and no
rainbow near-resolution theorem.  The exact remaining object is the
cross-parent, common-label Gram minimum in Section 7.  It is precisely
CPCR, rather than a within-packet or common-order gate.

## 1. Physical trace normal form

Use the physical coordinates

\[
                         (a_i,b_i),\qquad i\in[n],
\]

and write

\[
                         x_i=a_i,\qquad p_i=a_i\oplus b_i.
\]

At a pair boundary the physical point attached to \((p,x)\) is

\[
                         z(p,x)=(a=x,b=x\oplus p).
\]

The exact paired lift restricts \(p\) to the even shore.  If
\(d_{n,p}(x)\) is the outgoing coarse direction, the first physical edge
is \(b_{d_{n,p}(x)}\), and the pair midpoint is

\[
                         z(p,x)\oplus e_{b_{d_{n,p}(x)}}.
\]

Thus every physical owner has a unique representation

\[
                         (p,x,\rho),\qquad
 p\in E_n,\quad x\in Q_n,\quad \rho\in\{0,1\},
\]

where \(\rho=0\) is a pair boundary and \(\rho=1\) is the following
midpoint.  The column complete-mapping theorem is exactly what gives
uniqueness on the midpoint shore.  The number of representations is

\[
                         2^{n-1}2^n2=2^{2n}=K.
\]

For \(\ell<R\), let

\[
 \tau^{(n)}_{\ell,\rho}(p,x)
       \in\bigl(\{0,1,*\}^{\{a,b\}}\bigr)^n
\]

be the physical face of the next \(\ell\) edges.  In a local column a
star records that the corresponding physical direction occurs, and a
zero or one records the initial physical bit when that direction does not
occur.

For two local column symbols \(u,v\), put

\[
 w_{U,V}(u,v)
 =U^{\#\{c\in\{a,b\}:u_c=v_c=*\}}
  V^{\#\{c\in\{a,b\}:u_c,v_c\in\{0,1\},\ u_c\ne v_c\}}.
\]

Then the product of \(w_{U,V}\) over the \(n\) coarse columns is
\(U^aV^\delta\), where \((a,\delta)\) is exactly the affine pair type of
the two physical faces.

## 2. Exact binary transfer recursion

The recursion must remember four parity bits.  For

\[
 \kappa=|p|\pmod2,\quad c=|x|\pmod2,
 \qquad
 \kappa'=|p'|\pmod2,\quad c'=|x'|\pmod2,
\]

define

\[
\begin{aligned}
 B_n[\ell,\rho,\kappa,c;&\ell',\rho',\kappa',c'](U,V)\\
 ={}&\sum_{\substack{|p|=\kappa,\ |x|=c\\
                     |p'|=\kappa',\ |x'|=c'}}
 \prod_{i=1}^n
 w_{U,V}\bigl(
  \tau^{(n)}_{\ell,\rho}(p,x)_i,
  \tau^{(n)}_{\ell',\rho'}(p',x')_i
 \bigr).
\end{aligned}
\]

All displayed parities are modulo two.

Suppose \(n=2h\).  For a window parameter \((\ell,\rho,c)\), let

\[
 I_{\ell,\rho}=\{\rho,\rho+1,\ldots,\rho+\ell-1\}.
\]

At expanded-edge time \(t\), the coarse move number is
\(\lfloor t/2\rfloor\), and the parity recursion sends it to child
\(j\in\{0,1\}\) precisely when

\[
                         \lfloor t/2\rfloor\equiv j-c\pmod2.
\]

Define

\[
\begin{aligned}
 I_j(\ell,\rho,c)
   &:=\{t\in I_{\ell,\rho}:
          \lfloor t/2\rfloor\equiv j-c\pmod2\},\\
 \ell_j(\ell,\rho,c)&:=|I_j(\ell,\rho,c)|,\\
 \rho_j(\ell,\rho,c)&:=
 \begin{cases}
  \min I_j(\ell,\rho,c)\pmod2,&I_j\ne\varnothing,\\
  0,&I_j=\varnothing.
 \end{cases}
\end{aligned}
\]

The subsequence seen in child \(j\) is a consecutive child physical
interval of this length and starting phase.  Therefore the face itself
splits exactly as

\[
 \tau^{(n)}_{\ell,\rho}(p,x)
 =\tau^{(h)}_{\ell_0,\rho_0}(p_0,x_0)
  \oplus
  \tau^{(h)}_{\ell_1,\rho_1}(p_1,x_1).
\]

### Theorem 2.1 (full pair-enumerator recursion)

With \((\ell_j,\rho_j)\) formed from \((\ell,\rho,c)\), and
\((\ell'_j,\rho'_j)\) formed from \((\ell',\rho',c')\), one has

\[
\boxed{
\begin{aligned}
 B_n[\ell,\rho,\kappa,c;&\ell',\rho',\kappa',c']
  =\sum_{\alpha,\beta,\alpha',\beta'\in\{0,1\}}
   B_h[\ell_0,\rho_0,\alpha,\beta;
       \ell'_0,\rho'_0,\alpha',\beta']\\
 &\hspace{23mm}\cdot
   B_h[\ell_1,\rho_1,\kappa\oplus\alpha,c\oplus\beta;
       \ell'_1,\rho'_1,
       \kappa'\oplus\alpha',c'\oplus\beta'].
\end{aligned}}
\]

At \(n=4\), the base is explicit.  Put

\[
 K_0=\langle1111,0101\rangle,
\]

let \(\delta(y)\) be the coset direction table

\[
 \delta^{-1}(1)=K_0,
 \quad\delta^{-1}(2)=e_1+K_0,
 \quad\delta^{-1}(3)=e_1+e_2+K_0,
 \quad\delta^{-1}(4)=e_1+e_2+e_3+K_0,
\]

and put \(d=\delta(Sp\oplus x)\),
\(x_1=x\oplus e_d\), and
\(d_1=\delta(Sp\oplus x_1)\).  The only bottom traces needed in the
range below are

\[
\begin{array}{c|c|c}
\rho&\ell&\text{varied physical directions}\\ \hline
0&0&\varnothing\\
0&1&b_d\\
0&2&b_d,a_d\\
1&1&a_d\\
1&2&a_d,b_{d_1}.
\end{array}
\]

Their fixed symbols are the corresponding entries of
\(z(p,x)\) for \(\rho=0\), and of
\(z(p,x)\oplus e_{b_d}\) for \(\rho=1\).  Substitution in the defining
finite sum for \(B_4\) is the complete base polynomial; no unspecified
factor or choice remains.

#### Proof

The branch in the recursive rotor depends only on \(x\), and successive
coarse moves alternate children.  Deleting the moves of the other child
therefore leaves a consecutive trajectory in the selected child.  The
four parent parity constraints split as

\[
 \kappa_0\oplus\kappa_1=\kappa,
 \qquad c_0\oplus c_1=c,
\]

and similarly for the primed start.  Since the physical coordinates of
the two children are disjoint, both \(a\) and \(\delta\) add, so their
generating monomials multiply.  Summing over the four independent left
parities gives the displayed recurrence.  The seed table follows
directly from the audited \(Q_4\) factor and the adjacent expansion
\(i\mapsto(b_i,a_i)\).  \(\square\)

At the root define

\[
 \mathscr B_{n,q}(U,V)
 =\sum_{\rho,\rho',c,c'\in\{0,1\}}
 B_n[q,\rho,0,c;q,\rho',0,c'](U,V).
\]

Literal trace injectivity says that the only equal-face ordered pairs are
the \(K\) diagonal pairs.  Hence the requested enumerator is exactly

\[
 \boxed{
 A_{q,\epsilon}(a,\delta)
 =[U^aV^\delta]
  \bigl(\mathscr B_{n,q}(U,V)-KU^q\bigr).}
\]

The abstract lower and upper faces are the same face; only their external
Johnson interpretation differs.  Reversing every cycle merely reindexes
the same unoriented \(q\)-edge path faces.  Thus

\[
                         A_{q,-}=A_{q,+}=A_q,
\]

and the same equality holds for the two canonical orientations.

For \(q=o(n)\), a bottom leaf sees at most two physical edges.  Therefore
the five displayed seed rows are sufficient uniformly for all
\(q\le A\sqrt m\) at the calibrated packet scale.

## 3. The common-label stacked enumerator

Separate marginal polynomials are not enough for CPCR.  Let
\(\mathcal Q\subseteq[H]\times\{-,+\}\) be any set of protected rows and
replace the local symbol at physical coordinate \(r\) by the vector

\[
 \mathbf c_r(p,x,\rho)
 =\bigl(\tau^{(n)}_{q,\rho}(p,x)_r:
                    (q,\epsilon)\in\mathcal Q\bigr).
\]

The two sign entries at a fixed depth coincide abstractly.  Introduce an
indeterminate \(Z_{\mathbf u,\mathbf v}\) for every ordered pair of such
stacked column symbols, and in the definition of \(B_n\) replace
\(w_{U,V}(u,v)\) by \(Z_{\mathbf u,\mathbf v}\).  The proof of Theorem
2.1 is unchanged: child stacks concatenate and column monomials multiply.

This gives an exact multivariate transfer polynomial whose exponent
vector is the complete common-depth column-pair histogram.  Allowing an
arbitrary function of a finite list of starts gives, by the same
recursion, every higher column-type enumerator.  This is the correct
object for one affine label: one column permutation and one columnwise
complement act simultaneously on the entire vector symbol.  Multiplying
separate depth enumerators would incorrectly allow different affine
labels at different depths.

## 4. A surviving non-antipodal atom

The \(n\) coarse coordinates are partitioned into \(n/4\) bottom
\(Q_4\)-leaves.  A physical length-\(q\) interval starting in phase
\(\rho\) intersects exactly

\[
 d_\rho(q)=\left\lfloor{\rho+q-1\over2}\right\rfloor+1
\]

coarse moves.  For \(d_\rho(q)\le n/4\), recursive alternation sends
these moves to distinct bottom leaves.

Fix a root start \((p,x,\rho)\), and let \(V\) be the union of its
visited leaves.  Then

\[
                         |V|=4d_\rho(q).
\]

Choose any weight-two vector \(\alpha\in Q_n\) supported in
\([n]\setminus V\), and replace

\[
                         (p,x,\rho)
 \longmapsto(p\oplus\alpha,x,\rho).
\]

The new context is still even.  The binary schedule is unchanged because
it depends only on \(x\).  Every visited leaf sees the same local context,
so every direction in the protected window is unchanged.  In physical
coordinates the two initial points differ only in the two \(b\)-columns
of \(\alpha\); those columns lie outside the direction support.  The two
faces consequently have type

\[
                         (a,\delta)=(q,2).
\]

There are \(\binom{n-4d_\rho(q)}2\) choices.  Half of the \(K\) starts
have each value of \(\rho\), proving the lower bound in Section 0.

This is genuinely different from the antipodal mate.  In the protected
range \(R-q\to\infty\), its disagreement number is two rather than
\(R-q\).

## 5. Antipodal contraction does not give low codegree

Let

\[
                         V_{R,q}=\binom Rq2^{R-q}
\]

be the number of abstract physical \(q\)-faces.  In the full affine
catalogue \(\Gamma_R=Q_R\rtimes S_R\), one face has degree

\[
                         D_q=|\Gamma_R|{K\over V_{R,q}}.
\]

Every compiler image is closed under face antipodes.  Contract
\(f\) and \(\bar f\) to one supervertex.  The degree remains \(D_q\),
and every option edge has size \(K/2\).

For two nonantipodal supervertices represented by faces of type
\((a,\delta)\), affine double counting gives

\[
 {d_2([f],[f'])\over D_q}
 ={A_q(a,\delta)\over K M_{R,q}(a,\delta)},
\]

where

\[
 M_{R,q}(a,\delta)
 =\binom qa\binom{R-q}{q-a}2^{q-a}
   \binom{R-2q+a}{\delta}.
\]

Taking \((a,\delta)=(q,2)\) and using Section 4 gives

\[
 \boxed{
                         \Delta_2\ge(1/4-o(1))D_q.}
\]

The trivial upper bound \(\Delta_2\le D_q\) therefore determines the
post-contraction maximum-codegree scale exactly:

\[
                         \Delta_2=\Theta(D_q).
\]

This refutes any local nibble or rainbow criterion requiring
\(\Delta_2=o(D_q)\), and a fortiori the stronger growing-uniformity
condition \(\Delta_2=o(D_q/K)\).  Antipodes were not the only
degree-scale correlation; they were only the unique coordinate-free
deterministic pair.

There is also an unavoidable mixed-depth atom.  Every \(q\)-window has
exactly two containing \((q+1)\)-windows in the same cycle catalogue,
whereas an ambient \(q\)-face has \(2(R-q)\) containing
\((q+1)\)-faces.  Hence, under the affine catalogue, a compatible nested
pair has exact conditional codegree

\[
                         {1\over R-q}.
\]

This remains present in the common-label stack and shows why separate
depth matchings cannot be multiplied together.

## 6. What the dispersed selector does and does not do

Consider one dimension-typical product cell \(Q_S\).  The dispersed
selector partitions its axes into \(R\) groups and chooses one matching
direction from every group.  Conditional on a fixed \(q\)-face using
\(q\) distinct groups, a second same-support face with disagreements on
two further cell axes belongs to the same packet only when those axes
occupy two distinct unused groups and are the selected directions there.
The exact product law, averaged over the balanced group design, is

\[
 (1+o(1)){\binom{R-q}{2}\over\binom{S-q}{2}}.
\]

Complete affine batching then gives the packet-relative type census

\[
 \boxed{
 \eta_{q,2}(S)
 =(1+o(1))
 {\binom{R-q}{2}\over\binom{S-q}{2}}
 {A_q(q,2)\over K\binom{R-q}{2}}.}
\]

Thus

\[
                         \eta_{q,2}(S)
 \ge(1/4-o(1))(R/S)^2.
\]

More generally, a pair of relative type \((a,\delta)\) requires

\[
                         b=q-a+\delta
\]

new active axes beyond the first face.  Away from group collisions its
packet-relative mean is

\[
 (1+o(1)){(R-q)_b\over(S-q)_b}
 {A_q(a,\delta)\over K M_{R,q}(a,\delta)}.
\]

This formula is the precise fusion of the compiler enumerator with the
selector census.  It explains both sides of the audit.

* Because \(R=o(S)\), every fixed noncontracted pair receives an outer
  dilution once at least one new active axis is required.
* The dilution is only polynomial.  For the type-\((q,2)\) atom it is
  \(\Theta((R/S)^2)\), still exponentially larger than \(1/K\).
* The selector theorem establishes these identities as support-class
  averages and safe-profile censuses.  It does not give a quenched
  maximum over arbitrary cross-parent target pairs or arbitrary literal
  weights.
* The antipodal involution depends on the packet's full active support.
  Consequently antipodal contraction is color-local and does not define
  a common quotient of the global target layer.

Therefore the local degree-scale obstruction does not itself imply an
\(\Omega(W)\) CPCR deficit, while the selector dilution does not verify a
growing-uniformity rainbow theorem.  The two statements concern different
levels of the construction.

## 7. Exact alignment with CPCR

For one legal resolution state and one common affine label \(g_P\) per
packet, put

\[
 K_{PP'}^{q,\epsilon}(g,h)
 =|I_{P,g,q}^{\epsilon}\cap I_{P',h,q}^{\epsilon}|.
\]

Since every packet image is a set, one has exactly

\[
 \sum_TL_q^\epsilon(T)(L_q^\epsilon(T)-1)
 =\sum_{P\ne P'}K_{PP'}^{q,\epsilon}(g_P,g_{P'}).
\]

Using \(\sum_TL_q^\epsilon(T)=G\), the CPCR summand is therefore

\[
\boxed{
 \sum_T(L_q^\epsilon(T)-c_q)(L_q^\epsilon(T)-c_q-1)
 =\sum_{P\ne P'}K_{PP'}^{q,\epsilon}(g_P,g_{P'})
  -2c_qG+c_q(c_q+1)N_q.}
\]

Define the common-label cross-parent Gram kernel

\[
 \mathcal K_{PP'}(g,h)
 =\sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
   K_{PP'}^{q,\epsilon}(g,h).
\]

The transfer polynomial of Sections 2--3 computes the local column part
of this kernel once the relative physical embedding of \(P\) and \(P'\)
is fixed.  The selector census computes its annealed support-type
marginals.  Neither computes or bounds the quenched cross-parent minimum

\[
\begin{aligned}
 \mathfrak D_m:=\min_{\substack{
      \text{legal rank frames, selectors, slab trades}\\
      g_P\in\Gamma_R\ \text{one per packet}}}
 \sum_{q\le H,\epsilon}
 \left[
  \sum_{P\ne P'}K_{PP'}^{q,\epsilon}(g_P,g_{P'})
  -2c_qG+c_q(c_q+1)N_q
 \right].
\end{aligned}
\]

Every bracketed total is nonnegative after summing its target loads, and

\[
                         \mathrm{CPCR}\quad\Longleftrightarrow\quad
                         \mathfrak D_m=o(W).
\]

This is the exact remaining integral discrepancy.  It is cross-parent,
uses one affine label at all depths and both signs, and allows the legal
\(Q_{R+1}\) slab trades.  No common-order syndrome, within-packet trace,
owner, or component-count issue remains.

## 8. Certified boundary

Proved here:

1. an exact binary transfer computation of every
   \(A_{q,\epsilon}(a,\delta)\);
2. its exact extension to stacked depths and signs under one affine
   label;
3. a uniform nonantipodal lower atom
   \(A_q(q,2)/(K\binom{R-q}{2})\ge1/4-o(1)\);
4. post-antipode maximum codegree \(\Theta(D_q)\) in the local affine
   catalogue;
5. the exact packet-relative selector dilution formula; and
6. the exact cross-parent Gram formulation equivalent to CPCR.

Not proved here:

1. a quenched cross-parent degree/codegree theorem;
2. a rainbow near-resolution for the colored compiler hypergraph;
3. an \(\Omega(W)\) global type-count obstruction; or
4. CPCR.

The new substantive conclusion is negative for the proposed
antipode-contraction nibble route, but not for coefficient one.  The
remaining positive route must exploit cancellation and transport in the
cross-parent common-label Gram kernel, rather than local low codegree.
