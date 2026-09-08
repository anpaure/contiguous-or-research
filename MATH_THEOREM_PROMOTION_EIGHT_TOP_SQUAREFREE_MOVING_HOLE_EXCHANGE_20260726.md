# Promotion rings: a squarefree eight-top moving-hole exchange

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad H\ge2,
 \qquad M-3\ge6H.
\tag{0.1}
\]

There are eight tops, and two selections of one literal one-hole cyclic
frame at each top, with all of the following properties.

1. Each selection is a squarefree retained-middle owner packing.
2. The two selections have exactly the same retained-middle load.
3. At every lower depth \(1\le q\le H\), their load difference is one
   alternating eight-cell cube
   \[
      \Delta_q=-\Gamma_{K_q},\qquad
      \|\Delta_q\|_2^2=8,
   \tag{0.2}
   \]
   on a nested family of target chains.
4. At every upper depth \(1\le q<H\), the difference is a pair of
   disjoint eight-cell cubes and has squared norm \(16\). At \(q=H\)
   it is zero.

Thus the exact two-sided untagged action is

\[
                         8H+16(H-1)=24H-16.
\tag{0.3}
\]

For a lower-rank ambient load \(\lambda_q\), the exact floor-energy
change is

\[
 \boxed{
 \Phi_q(\lambda_q+\Delta_q)-\Phi_q(\lambda_q)
 =\langle\lambda_q,\Delta_q\rangle+4.}
\tag{0.4}
\]

The upper analogue is \(\langle\lambda_q^+,\Delta_q^+\rangle+8\).
Hence this is a genuine non-load-neutral, squarefree, owner-preserving
compound direction. It is favorably oriented exactly when its ambient
cube correlation beats the displayed self-toll. No theorem below forces
that inequality in every positive-energy state, so coefficient one is
not claimed.

The construction uses different deleted phases in its two frame
patterns. It therefore escapes the full/common-hole cube rigidity proved
in
`MATH_THEOREM_PROMOTION_TWO_TOP_MOVING_HOLE_TRANSFER_AND_CUBE_RIGIDITY_20260726.md`.
It belongs to the unrestricted physical frame catalogue. The two long
run reversals are not shown to preserve the fixed mechanical support.

This theorem settles the requested **common-base cube** branch, not
absolute support minimality. The independent two-base conveyor theorem
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md` gives a
smaller three-top squarefree exchange; one top is impossible and the
arbitrary two-top case remains open.

## 1. Three separated placeholders

Partition a core \(C\) into three labelled linear runs

\[
                         C=R_1\mathbin{\dot\cup}R_2
                              \mathbin{\dot\cup}R_3,
 \qquad |R_s|=L_s\ge2H.
\tag{1.1}
\]

Write

\[
\begin{aligned}
 R_1&=(z,y_0,y_1,\ldots,y_{L_1-2}),\\
 R_2&=(u_0,u_1,\ldots,u_{L_2-1}),\\
 R_3&=(v_0,v_1,\ldots,v_{L_3-1}).
\end{aligned}
\tag{1.2}
\]

On the abstract alphabet \(C\cup\{A_1,A_2,A_3\}\), define

\[
\begin{aligned}
 \alpha={}&(A_1,
 z,y_0,\ldots,y_{L_1-2},
 A_2,
 u_0,\ldots,u_{L_2-1},
 A_3,
 v_0,\ldots,v_{L_3-1}),\\
 \beta={}&(A_1,
 y_0,\ldots,y_{L_1-2},z,
 A_2,
 u_{L_2-1},\ldots,u_0,
 A_3,
 v_{L_3-1},\ldots,v_0).
\end{aligned}
\tag{1.3}
\]

Thus \(R_1\) undergoes the moving-seam shift, while \(R_2,R_3\) are
reversed. The three placeholders are separated by at least \(2H\) core
labels, so no cyclic \(H\)-window contains two placeholders.

In \(\alpha\), delete the phase whose middle omitted interval is

\[
                         E_L=\{z,y_0,\ldots,y_{H-2}\}.
\tag{1.4}
\]

In \(\beta\), delete the phase whose middle omitted interval is

\[
                         E_R=\{y_{L_1-H},\ldots,y_{L_1-2},z\}.
\tag{1.5}
\]

As in the promotion convention, a phase is indexed by the terminal
endpoint of its omitted interval. Hence at another signed rank the
deleted interval changes length but keeps that terminal endpoint.

For \(r=1,2,3\), choose two labels \(a_{r,0},a_{r,1}\notin C\), all six
distinct. For \(\varepsilon\in\{0,1\}^3\), put

\[
 U_\varepsilon=C\cup
 \{a_{1,\varepsilon_1},a_{2,\varepsilon_2},
                         a_{3,\varepsilon_3}\}.
\tag{1.6}
\]

Specializing \(A_r\mapsto a_{r,\varepsilon_r}\) gives punctured frames
\(\alpha_\varepsilon^-\) and \(\beta_\varepsilon^-\) on this top.
Define the two eight-frame shores

\[
\begin{aligned}
 \mathcal O&=\{\alpha_\varepsilon^-:|\varepsilon|\ {m even}\}
       \cup\{\beta_\varepsilon^-:|\varepsilon|\ {m odd}\},\\
 \mathcal N&=\{\beta_\varepsilon^-:|\varepsilon|\ {m even}\}
       \cup\{\alpha_\varepsilon^-:|\varepsilon|\ {m odd}\}.
\end{aligned}
\tag{1.7}
\]

Both shores choose one actual repaired frame at each of the same eight
tops.

## 2. Exact cube derivative with a moving hole

For \(K\subseteq C\), put

\[
 \Gamma_K=\sum_{\varepsilon\in\{0,1\}^3}
 (-1)^{|\varepsilon|}
 e_{K\cup\{a_{1,\varepsilon_1},a_{2,\varepsilon_2},
                         a_{3,\varepsilon_3}\}}.
\tag{2.1}
\]

It has eight distinct coordinates, four with each sign, and

\[
                         \|\Gamma_K\|_2^2=8.
\tag{2.2}
\]

For an abstract punctured pattern \(\gamma^-\), let
\(\mathcal Q_h^-(\gamma)\) be its retained length-\(h\) intervals which
contain no placeholder. The checkerboard specialization has the exact
load

\[
 \mathcal A_h(\gamma^-)
 =\sum_{Q\in\mathcal Q_h^-(\gamma)}\Gamma_{C\setminus Q}.
\tag{2.3}
\]

Indeed, if an omitted interval contains placeholder \(A_r\), its
complementary target omits \(a_{r,\varepsilon_r}\) and is independent of
\(\varepsilon_r\), so the alternating sum in that coordinate is zero.
If the interval is the core-only set \(Q\), its alternating target sum
is exactly \(\Gamma_{C\setminus Q}\).

### Theorem 2.1 (exact all-depth action)

The middle load difference \(\mathcal N-\mathcal O\) is zero. For every
\(1\le q\le H\), put

\[
\begin{aligned}
 h_q&=H+q,\\
 Q_q^-&=\{z,y_0,\ldots,y_{h_q-2}\},\\
 K_q^-&=C\setminus Q_q^-.
\end{aligned}
\tag{2.4}
\]

At lower rank \(m-q\),

\[
                         \boxed{\Delta_q^-=-\Gamma_{K_q^-}.}
\tag{2.5}
\]

The sets \(K_q^-\) satisfy

\[
 |K_q^-|=m-q-3,
 \qquad K_{q+1}^-=K_q^-\setminus\{y_{H+q-1}\}.
\tag{2.6}
\]

For \(1\le q<H\), put \(h=H-q\) and

\[
\begin{aligned}
 Q_q^{\rm L}&=\{z,y_0,\ldots,y_{h-2}\},\\
 Q_q^{\rm D}&=\{y_{q-1},\ldots,y_{H-2}\},\\
 K_q^{\rm L}&=C\setminus Q_q^{\rm L},
 \qquad K_q^{\rm D}=C\setminus Q_q^{\rm D}.
\end{aligned}
\tag{2.7}
\]

At upper rank \(m+q\),

\[
 \boxed{\Delta_q^+=\Gamma_{K_q^{\rm D}}-Gamma_{K_q^{\rm L}},
        \qquad \|\Delta_q^+\|_2^2=16.}
\tag{2.8}
\]

At \(q=H\), the upper action is zero.

#### Proof

At complementary length \(H\), the core-only windows within \(R_1\)
are the same in the two patterns except for the left end window of
\(\alpha\) and the right end window of \(\beta\). These are precisely
the two deleted windows (1.4)--(1.5). Reversing \(R_2\) or \(R_3\)
does not change its family of interval sets at any length. Therefore

\[
                         \mathcal Q_H^-(\alpha)
                         =\mathcal Q_H^-(\beta).
\tag{2.9}
\]

Equation (2.3) proves zero middle action. Global complementation turns
the direct middle owners into the root-form middle targets, so the same
identity holds in either convention.

Now take \(h=H+q>H\). The deleted \(\alpha\)-phase has terminal endpoint
\(y_{H-2}\); its length-\(h\) interval crosses \(A_1\), so it deletes no
core-only interval. The deleted \(\beta\)-phase ends at \(z\) and removes
the exceptional right length-\(h\) interval of \(R_1\). All internal
intervals in \(R_1\) pair, and the reversed runs have identical decks.
The sole retained core interval on the \(\alpha\) side without a mate is
\(Q_q^-\). Thus the retained core deck of \(\beta\) minus that of
\(\alpha\) is \(-Q_q^-\). Equations (2.3) and (1.7) give (2.5).
The rank and nesting in (2.6) follow from
\(|C|=M-3\) and \(M-H=m\).

For \(h=H-q<H\), the deleted \(\alpha\)-phase removes the internal
interval \(Q_q^{\rm D}\), while the deleted \(\beta\)-phase removes the
exceptional right interval. The complete \(R_1\)-decks differ only by
the exceptional left and right intervals. Hence the retained
\(\beta\)-deck minus the retained \(\alpha\)-deck is

\[
                         Q_q^{\rm D}-Q_q^{\rm L}.
\]

This gives (2.8). Its two cube supports are disjoint because
\(Q_q^{\rm L}\) contains \(z\) and \(Q_q^{\rm D}\) does not. At
\(q=H\), the omitted interval is empty and every target is its top,
independent of frame and hole. \(\square\)

## 3. Squarefree middle ownership

We now verify the point which the bare two-top seam fails.

### Lemma 3.1 (placeholder-neighborhood separation)

For each \(r\in\{1,2,3\}\), no abstract \(H\)-window containing
\(A_r\) in \(\alpha\) has the same core-label set as an \(H\)-window
containing \(A_r\) in \(\beta\).

#### Proof

Let \(P\) be the core run preceding \(A_r\), and \(Q\) the run following
it. An \(H\)-window containing \(A_r\) has, for one unique
\(0\le k\le H-1\), the form

\[
 \operatorname{suffix}_k(P)\cup\{A_r\}\cup
 \operatorname{prefix}_{H-1-k}(Q).
\tag{3.1}
\]

Because the three runs have disjoint label sets, equality between an
\(\alpha\)-window and a \(\beta\)-window first forces the same value of
\(k\).

For \(R_1\), every nonempty prefix changes from

\[
 \{z,y_0,\ldots,y_{t-2}\}
 \quad\hbox{to}\quad
 \{y_0,\ldots,y_{t-1}\},
\tag{3.2}
\]

and every nonempty suffix changes by replacing its first included
\(y\)-label with \(z\). For \(R_2,R_3\), reversal exchanges a prefix of
length \(t\) with the opposite suffix. Since \(|R_s|\ge2H\), those two
sets are disjoint whenever \(1\le t\le H-1\).

At \(A_1\), the preceding run \(R_3\) is reversed and the following run
\(R_1\) is shifted. At \(A_2\), the preceding run is shifted and the
following run \(R_2\) is reversed. At \(A_3\), both adjacent runs are
reversed. If \(k=0\), the nonempty following segment changes; if
\(k=H-1\), the nonempty preceding segment changes; and for intermediate
\(k\) both do. Therefore (3.1) can never agree. \(\square\)

### Theorem 3.2 (both shores are squarefree)

No two distinct frames within \(\mathcal O\) share a retained middle
owner. The same holds for \(\mathcal N\).

#### Proof

Take two distinct cube vertices \(\varepsilon,\delta\). A common middle
owner is contained in \(U_\varepsilon\cap U_\delta\). Hence its omitted
\(H\)-window in each frame must contain the selected variable label in
every coordinate on which \(\varepsilon\) and \(\delta\) differ.

If the two frames use the same abstract pattern, their cube vertices
have the same parity and therefore Hamming distance two. This would
require an \(H\)-window containing two placeholders, impossible by
(1.1)--(1.3).

If they use different patterns, the vertices have opposite parity and
their distance is one or three. Distance three is impossible for the
same reason. At distance one, say in coordinate \(r\), a common owner
would give an \(H\)-window containing \(A_r\) in each pattern with the
same core-label set. No other placeholder can occur in either window.
Lemma 3.1 excludes the equality. Deleting phases can only remove owners,
so both repaired shores are squarefree. \(\square\)

Combining Theorems 2.1 and 3.2 proves that (1.7) is a legal compound
exchange inside the squarefree one-hole owner-packing fibre.

## 4. Exact floor derivative

For an integer load \(\lambda\) and a zero-sum \(\{-1,0,1\}\)-vector
\(d\),

\[
 \sum_S\binom{\lambda(S)+d(S)}2-sum_S\binom{\lambda(S)}2
 =\langle\lambda,d\rangle+\frac12\|d\|_2^2.
\tag{4.1}
\]

Any fixed floor correction differs from collision energy by a constant
and a linear function of the total load. Since the compound exchange
preserves total load at every rank, (4.1) is also its exact floor-energy
change. Equations (2.2), (2.5), and (2.8) give

\[
\begin{aligned}
 \Phi_q^-(\lambda_q^-+\Delta_q^-)-\Phi_q^-(\lambda_q^-)
 &=\langle\lambda_q^-,\Delta_q^-\rangle+4,
       &&1\le q\le H,\\
 \Phi_q^+(\lambda_q^++\Delta_q^+)-\Phi_q^+(\lambda_q^+)
 &=\langle\lambda_q^+,\Delta_q^+\rangle+8,
       &&1\le q<H.
\end{aligned}
\tag{4.2}
\]

Thus a weighted two-sided energy with weights \(w_q^\pm\ge0\) decreases
in the displayed orientation exactly when

\[
 \sum_{q=1}^H w_q^-
   \bigl(\langle\lambda_q^-,\Delta_q^-\rangle+4\bigr)
 +\sum_{q=1}^{H-1}w_q^+
   \bigl(\langle\lambda_q^+,\Delta_q^+\rangle+8\bigr)<0.
\tag{4.3}
\]

The isolated endpoints have equal intrinsic energy: transposing
\(a_{1,0}\) and \(a_{1,1}\) flips cube parity and maps \(\mathcal O\)
to \(\mathcal N\). The sign in (4.3) is therefore a genuine correlation
with the rest of the physical state. No automatic descent is asserted.

### Proposition 4.1 (a literal squarefree descent witness)

Fix one lower depth \(1\le q\le H\) and one negative target \(T_-\) of
\(\Delta_q^-\). There is one additional actual cyclic frame whose
middle deck is disjoint from the common middle support of both shores and
whose depth-\(q\) score against \(\Delta_q^-\) is exactly \(-1\).
Consequently the resulting nine-frame partial factor has exact floor
descent \(-1\) at that prescribed depth.

#### Proof

Every target in the derivative is contained in

\[
 \mathcal U=C\cup\{a_{r,b}:1\le r\le3,\ b\in\{0,1\}\}.
\tag{4.4}
\]

Choose fresh disjoint sets \(Z,Y\), outside \(\mathcal U\), with

\[
                         |Z|=H+1,\qquad |Y|=q-1.
\tag{4.5}
\]

There is enough room: \(|\mathcal U|=M+3\), while (0.1) implies
\(2m-(M+3)=m-H-3\ge2H\). Put

\[
                         U_e=T_-\mathbin{\dot\cup}Z
                                      \mathbin{\dot\cup}Y.
\tag{4.6}
\]

This is an \(M\)-set. Make \(T_-\) one consecutive block in a cyclic
order of \(U_e\), put a \(Z\)-label at each end of the block, and
separate the remaining \(Y\)-labels by \(Z\)-labels. Then \(T_-\) is
the unique length-\((m-q)\) interval containing no label of \(Z\).
Every derivative target avoids \(Z\), so the new frame has score exactly
\(-1\) against \(\Delta_q^-\).

Every direct middle \(m\)-window of the new frame contains a \(Z\)-label,
because its complementary \(H\)-window cannot contain all \(H+1\)
labels of \(Z\). Every direct middle owner of the eight-frame packet
avoids \(Z\). Thus adjoining the frame preserves middle squarefreeness
on both shores; global complementation gives the same conclusion in the
root-target convention. Finally, the two packet endpoints have equal intrinsic energy,
so their energy difference in this exterior is its score \(-1\). \(\square\)

## 5. Exact boundary

Proved here:

1. eight actual one-hole cyclic frames on each shore;
2. exact equality of their middle load vectors;
3. squarefreeness of both middle-owner shores;
4. exact lower action \(8H\), upper action \(16(H-1)\), and two-sided
   action \(24H-16\);
5. nested lower cube supports through every \(1\le q\le H\); and
6. the exact floor derivative (4.2)--(4.3); and
7. a literal middle-squarefree physical exterior producing strict
   descent at every prescribed lower depth.

Not proved here:

1. a statewise theorem forcing a negatively charged copy of (1.7);
2. a dense owner-disjoint packing or resolution of these exchanges;
3. compatibility with an arbitrary preassigned nested tag schedule;
4. positive-density availability inside the fixed mechanical atlas; or
5. coefficient one.

This removes the algebraic and squarefree-legality barriers for one
bounded compound direction. The surviving quantitative statement is a
charged-copy theorem: positive floor energy must force enough separated
three-placeholder cubes for which (4.3) is negative, or else supply a
dual obstruction to that assertion.
