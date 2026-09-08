# Audit of the \(Q_4\) four-shore composition and trace boundary

Date: 2026-07-26

Method: exact algebra only; no computation or search.

Audited source: MATH_ATTACK_K_Q4_FOUR_SHORE_COMPOSITION_AND_TRACE_BOUNDARY_20260726.md.

## 0. Verdict

The following claims pass:

1. the intrinsic absence of a common rooted \(\mathbb Z_8\) phase;
2. Proposition 2.1 and its suspension scope;
3. the \(12/16\) owner-legality law;
4. Proposition 3.2, including the stronger assertion that **any**
   same-owner \(AB\)-partner forces both selectors to be constant;
5. the exact count \(12^{2^h/64}\); and
6. all changed-tail constants attached to that count.

The fixed-wire support bound \(L_d\le h2^d\) also passes.  Its conversion
to the trace proportion \(2h/2^d\) is valid for the aligned affine
parity-lift trace model, where the trace is determined by the completed
support and two outside bit strings.  The assertion that this
automatically transfers fibrewise through an arbitrary-\(k\) carrier
needs one additional frozen-fibre trace-decomposition lemma.  Without
that interface, Theorem 6.1 is stated too broadly.

The globally constant \(AB\) syndrome-kernel collision was added with the
correct scope: it is valid for a constant shore and is explicitly not
claimed for the nonconstant twelve-state atlas.

## 1. No common \(\mathbb Z_8\) phase

Suppose \(c:Q_4\to\mathbb Z_8\) advanced by one on every edge of every
shore.  Modulo four, \(c-c_4\) is invariant on the union of the shore
graphs.  This union contains every edge of \(Q_4\): at each syndrome
phase the shore group supplies both directions having the required
syndrome column, and every cube edge is oriented from one of its two
endpoints at the corresponding phase.  Hence the union is connected and

\[
                         c(x)=c_4(x)+4r(x)
\]

after an additive normalization, with \(r:Q_4\to\mathbb F_2\).

Across the first three syndrome transitions there is no wrap in the
chosen representatives \(0,1,2,3\), so \(r\) must be unchanged.  On the
phase-zero fibre, the two possible first directions are \(1,3\), giving
invariance under \(e_1+e_3\); transporting the phase-one invariance under
\(e_2+e_4\) back through a first edge makes \(r\) invariant under both
generators of the phase-zero fibre.  Thus it is constant there.  The
same transport makes it constant, with the same value, on the next three
fibres.  The transition \(3\to0\) must instead toggle \(r\), because
\(3+1=4\) in \(\mathbb Z_8\).  Contradiction.

Thus the bare four-shore cube has only the common \(\mathbb Z_4\) phase
and antipodal port.  Proposition 2.1 correctly withholds the ordinary
common-phase suspension.

## 2. The \(12/16\) law

On a genuine label plane write

\[
 \alpha(x,y)=U(y),\qquad \beta(x,y)=V(x).
\]

At a prefix cutting both coordinate pairs, the owner-label map is

\[
                         T(x,y)=(x+U(y),\,y+V(x)).
\]

If \(U\) or \(V\) is constant, triangular inversion proves that \(T\) is
bijective.  If both are nonconstant, then

\[
 U(y)=y+u_0,\qquad V(x)=x+v_0,
\]

and

\[
 T(x,y)=(x+y+u_0,\,x+y+v_0)
\]

has image size two.  Therefore

\[
 \boxed{(U(0)+U(1))(V(0)+V(1))=0}
\]

is necessary and sufficient, leaving exactly twelve legal states.

For the bare \(Q_4\),

\[
 (e_1+e_3)+(e_2+e_4)=\mathbf1.
\]

The four-label plane double-counts antipodal roots.  Descent requires
\(U(y+1)=U(y)\) and \(V(x+1)=V(x)\), so only the four global shores
\(I,A,B,AB\) survive.  The source distinguishes these two settings
correctly.

## 3. Same-owner \(AB\) criterion

Let \((U,V)\) and \((U',V')\) be legal charts and suppose

\[
                         d'(z)=AB\,d(z)
\]

at every physical owner.  Before the \(a\)-edge, both charts assign the
same row label to \(z\), so comparison of the \(A\)-controlled direction
forces

\[
                         U'(y)=1+U(y).               \tag{3.1}
\]

Before the \(b\)-edge the two row labels at one owner differ by the
\(A\)-displacement, so comparison of the \(B\)-directions gives

\[
                         V'(x+1)=1+V(x).             \tag{3.2}
\]

Before the \(d\)-edge only the \(B\)-pair is cut.  The same comparison
gives

\[
                         V'(x)=1+V(x).               \tag{3.3}
\]

Equations (3.2)--(3.3) force \(V\) to be constant and \(V'=1+V\).  At
the middle boundary before \(c\), comparison of the \(A\)-directions,
together with (3.1), then forces \(U(y+1)=U(y)\).  Thus \(U\) is constant
and \(U'=1+U\).  Conversely constant complementary charts are global
Klein shores and satisfy the relation.

Proposition 3.2 therefore passes in its strongest form.  Eight of the
twelve legal states are nonconstant, and none has a same-owner
fixed-point-free partner inside this ansatz.

## 4. State count and action

For \(h=2^a\ge8\), put

\[
 N={2^h\over2h},\qquad t={h\over8}.
\]

The standard slabs

\[
 (8j,8j+2,8j+4,8j+6),\qquad 0\le j<t,
\]

are disjoint and use four coordinates from the repeated even syndrome
class.  Each quartet has \(N/4\) label planes and twelve independent
legal states on each plane.  Hence

\[
 12^{tN/4}
 =12^{(h/8)(2^h/(2h))/4}
 =\boxed{12^{2^h/64}}.
\]

For one plane, if \(u=U(0)+U(1)\) and \(v=V(0)+V(1)\) as integer sums,
the changed-tail count is \(8(u+v)\).  On the twelve legal states the
distribution is

\[
\begin{array}{c|ccccc}
\text{changed tails}&0&8&16&24&32\\ \hline
\text{number of states}&1&4&2&4&1.
\end{array}
\]

Thus the mean is \(16\), the maximum is \(32\), the global uniform mean
density is \(1/4\), and the maximum density is \(1/2\).  All constants
pass.

## 5. Constant-shore kernel and fixed-wire scope

For a globally constant \(AB\)-shore, every

\[
                         e\in E\cap K\cap\mathbb F_2^J
\]

gives the displayed collision

\[
                         p'=p+e,\qquad y'=y+ABe.
\]

Since \(E\) has codimension one and the standard syndrome kernel \(K\)
has codimension \(\log_2h\),

\[
 \dim(E\cap K\cap\mathbb F_2^J)
 \ge |J|-\log_2h-1.
\]

This argument does not use fixed points of \(AB\).  Its stated limitation
to a globally constant shore is necessary and correct.

For the row-dependent atlas, let \(\mathcal P\) be the fixed two-point
wire frame.  If \(s(J)\) wires meet \(J\) once, the orbit under the full
wire-swap group has size \(2^{s(J)}\); an allowed subgroup has orbit size
at most this.  Therefore

\[
                         |\operatorname{Orb}(J)|\le2^d,
\qquad                    L_d\le h2^d.               \tag{5.1}
\]

This support statement is unconditional.

In the aligned affine parity-lift model, appending the two outside
strings gives at most

\[
                         h2^d2^{2(h-d)}
\]

codes among \(2^{2h-1}\) starts, hence

\[
 \boxed{\text{distinct-code proportion}\le {2h\over2^d}}.       \tag{5.2}
\]

The arithmetic and the Gaussian-depth consequence pass.  What is not
proved solely by (5.1) is that an arbitrary outer carrier contributes no
additional trace-visible datum.  To transfer (5.2) fibrewise, one must
state and prove that after freezing tags, cell identity, exterior context,
and phase, the local trace is determined by \(J\) and the same two
outside strings, and that these frozen fibres preserve the start/code
normalization.  The synthesis currently asserts this interface rather
than deriving it.

## 6. Exact boundary

The four-shore cube eliminates the local fixed-coordinate defect, but:

* generic suspension is blocked by the intrinsic phase failure;
* high-entropy legal row charts lose the same-owner \(AB\) relation;
* a constant \(AB\)-shore retains the syndrome-kernel collision; and
* every fixed-frame row atlas retains the support-library bound.

The only correction needed in the synthesis is to qualify Theorem 6.1
and its arbitrary-\(k\) fibrewise application as an aligned-trace
interface statement.  All other audited claims and constants pass.
