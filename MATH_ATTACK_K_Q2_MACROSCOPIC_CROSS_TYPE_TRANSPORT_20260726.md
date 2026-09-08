# Macroscopic cross-type transport from the exact \(Q_2\) associator

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Fix a pairing of the \(2m\) ordinary coordinates and leave the remaining
coordinate \(\infty\) distinguished.

Uniform nested deletion gives the exact target type operator. At rank
\(m-j\), a type \((\varepsilon,f)\) loses one full pair with probability

\[
                         \frac{2f}{m-j}.
\tag{0.1}
\]

Its pair-death mass is

\[
               \frac{m-j-1}{2m+1}W
               =\left(\frac12+o_A(1)\right)W
\tag{0.2}
\]

per depth, uniformly for \(j\le A\sqrt m\).

Unbiased coordinate recoupling is a reversible birth--death chain, but its
relaxation time is \(\Theta(m)\). Hence \(O(\sqrt m)\) unbiased
recouplings do not mix the middle source law to a depth-\(A\sqrt m\)
target law.

The signed \(24\)-owner associator is biased: one visible shore switch
erases a Bernoulli-\(1/3\) contribution. The audited
product-transversal disjoint depth-\(q\) tensor therefore moves the mean
by at most \(q/3\), not the required \(q/2+O_A(1)\).

The main positive result is a nonproduct two-seed completion. On

\[
 \mathcal U=
 \left\{X\cup Y:
 X\in\binom{[6]}3,\quad
 Y\in\{uw,ux,vw,vx\}\right\},
\tag{0.3}
\]

there are four exact \(20Q_2\)-factors with lower ledgers

\[
\begin{array}{c|c}
00&32f_0+48f_1\\
10&48f_0+32f_1\\
01&48f_0+32f_1\\
11&64f_0+16f_1.
\end{array}
\tag{0.4}
\]

The upper ledgers are the identical shift
\(f_0,f_1\mapsto f_1,f_2\). Both Boolean bits have the same exact signed
action:

\[
                  16(e_0-e_1)\quad\hbox{below},
 \qquad           16(e_1-e_2)\quad\hbox{above}.
\tag{0.5}
\]

One common \(\mathbb Z_4\) colouring suspends all four factors on identical
support to twenty physical \(C_{2h}\)'s for every \(h\ge2\). A stable
first-eligible tensor packing puts \(W-e^{-\Omega(m)}W\) owners into
literal long-cycle packets with \(4^r\) resolutions and \(G/(2h)\)
components.

Pointwise, the carrier has two disjoint death classes of density \(1/5\)
each. Corner \(11\) erases a Bernoulli-\(2/5\) contribution. The
mean-sharp visibility demand is therefore

\[
 \boxed{
 L^*_{\varepsilon,q}
 =\frac52\Delta_{\varepsilon,q}
 =\frac{5q(2m-2\varepsilon-q-1)}{4(2m-1)}
 =\frac54q+O_A(1).}
\tag{0.6}
\]

Thus the requested macroscopic cross-type transport exists literally.
The direct tensor is not yet the complete Gaussian mixer: it sees only
\(q\) gadgets, has drift \(2q/5\), and is short by
\(q/10+O_A(1)\) type units. The exact successor is a \(5/4\)-visibility
braid, or a further retile removing half of the remaining \(1/5\)
survivor-high class.

## 1. Exact target and unbiased recoupling operators

A rank-\((m-j)\) target of type \((\varepsilon,f)\) has

\[
\begin{array}{c|ccc}
&\text{full}&\text{empty}&\text{split}\\ \hline
&f&f+j+\varepsilon&m-j-\varepsilon-2f.
\end{array}
\tag{1.1}
\]

Its orbit size is

\[
 T_j(\varepsilon,f)
 =\frac{2^{m-j-\varepsilon-2f}m!}
 {f!(f+j+\varepsilon)!(m-j-\varepsilon-2f)!}.
\tag{1.2}
\]

Deleting a uniformly chosen present coordinate gives

\[
\begin{array}{c|c}
(\varepsilon,f)\to(\varepsilon,f-1)&2f/(m-j),\\
(1,f)\to(0,f)&1/(m-j),\\
(\varepsilon,f)\to(\varepsilon,f)&
(m-j-\varepsilon-2f)/(m-j).
\end{array}
\tag{1.3}
\]

Counting ordered deletion flags proves \(\pi_jK_j=\pi_{j+1}\). One
uniform ordering of each middle set therefore realizes all target type
laws simultaneously at the fractional level.

The exact conditional-sector centre displacement is

\[
 \Delta_{\varepsilon,q}
 =\frac{q(2m-2\varepsilon-q-1)}{2(2m-1)}
 =\frac q2+O_A(1).
\tag{1.4}
\]

The infinity-death mass is \(1/(2m+1)\) per step, hence only
\(O_A(W/\sqrt m)=o(W)\) through the Gaussian window.

For comparison, choose two old coordinate pairs uniformly and then one of
their two non-old recouplings. Put

\[
 h=m-j-\varepsilon-2f.
\]

The exact death and birth probabilities are

\[
 d_{j,\varepsilon}(f)
 =\frac{f(f+j+\varepsilon)}{\binom m2},
 \qquad
 b_{j,\varepsilon}(f)
 =\frac{\binom h2}{2\binom m2}.
\tag{1.5}
\]

The target law conditional on \(\varepsilon\) is reversible, and

\[
 b_{j,\varepsilon}(f)-d_{j,\varepsilon}(f)
 =-\frac{2m-1}{m(m-1)}
   (f-\bar f_{j,\varepsilon}).
\tag{1.6}
\]

Thus the relaxation time is \(\Theta(m)\). On
\(z=4(f-\bar f)/\sqrt m\),

\[
 m(K-I)\varphi(z)
 \longrightarrow 2\varphi''(z)-2z\varphi'(z).
\tag{1.7}
\]

If \(q=A\sqrt m+O(1)\) and \(t=O(\sqrt m)\), martingale iteration of
(1.6) gives \((f_t-f_0)/\sqrt m\to0\) in probability. Since the source
and target limits are \(N(0,1)\) and \(N(-2A,1)\),

\[
 \liminf d_{\rm TV}(\mathcal L(f_t),\pi_q)
 \ge 2\Phi(A)-1>0.
\tag{1.8}
\]

So the useful operator must be signed, not frame-symmetric.

## 2. The one-seed signed operator

The exact \(24\)-owner associator has ledger

\[
                         16f_0+8f_1\longrightarrow24f_0.
\tag{2.1}
\]

With a spectator core \(C\), this is

\[
                         C+B\longmapsto C,
 \qquad                  B\sim{\rm Bernoulli}(1/3).
\tag{2.2}
\]

The reciprocal deletion and insertion kernels on \(N\) contributions are

\[
 D_N(j,j-1)=j/N,\qquad D_N(j,j)=1-j/N,
\tag{2.3}
\]

\[
 U_N(j,j+1)=1/3,\qquad U_N(j,j)=2/3.
\tag{2.4}
\]

Their heat-bath closure is reversible with stationary
\({\rm Bin}(N,1/3)\):

\[
 Q_N(j,j-1)=\frac{2j}{3N},
 \qquad
 Q_N(j,j+1)=\frac{N-j}{3N}.
\tag{2.5}
\]

Matching (1.4) requires \(3\Delta_{\varepsilon,q}
=3q/2+O_A(1)\) visible one-seed layers. The canonical
product-transversal disjoint tensor sees at most \(q\), leaves
\(q/6+O_A(1)\) mean error, and in the symmetric product model has
limiting total-variation gap

\[
                         2\Phi(A/3)-1.
\tag{2.6}
\]

## 3. Explicit two-seed completion

Let

\[
 Q_R=(uw,vw,vx,ux),\qquad
 M_{10}=13\mid24\mid56,\qquad
 M_{01}=12\mid35\mid46.
\tag{3.1}
\]

For \(M=\{r,p,q\}\), define \(\mathscr D(M;r)\) by:

* on the eight special sets splitting every \(M\)-pair, fix the
  orientation of \(r\), vary the endpoints of \(p,q\), and fix the
  reservoir orientation, giving eight \(Q_2\)'s;
* on the other twelve special sets, use vertical reservoir squares.

This is an exact \(20Q_2\)-factor. Put

\[
 \mathscr F_{00}=\{X\cup Q_R:X\in\tbinom{[6]}3\},
 \quad
 \mathscr F_{10}=\mathscr D(M_{10};56),
 \quad
 \mathscr F_{01}=\mathscr D(M_{01};12).
\tag{3.2}
\]

For \(\mathscr F_{11}\), use at every fixed reservoir orientation

\[
\begin{aligned}
 S_1&=(125,235,345,145),\\
 S_2&=(126,246,346,136),\\
 S_3&=(134,146,156,135),\\
 S_4&=(234,245,256,236).
\end{aligned}
\tag{3.3}
\]

Their direction pairs are

\[
                         13\mid24,\quad14\mid23,
                         \quad36\mid45,\quad35\mid46.
\tag{3.4}
\]

They partition sixteen special states. Put the remaining four states

\[
                         123,\quad124,\quad356,\quad456
\tag{3.5}
\]

on vertical reservoir squares. Hence all four corners partition the same
80 owners into twenty physical \(Q_2\)'s.

Relative to \(12\mid34\mid56\mid uv\mid wx\), define

\[
\begin{aligned}
 \mathcal A&=\{125,126,345,346\},\\
 \mathcal B&=\{134,234,156,256\},\\
 \mathcal C&=\{123,124,356,456\},\\
 \mathcal T&=\{135,136,145,146,235,236,245,246\}.
\end{aligned}
\tag{3.6}
\]

With compatible orientations, the touched-edge identity is pointwise:

\[
 f_{\epsilon_1,\epsilon_2}(X,Y)
 =f_{00}(X,Y)
 -\epsilon_1{\bf1}_{\mathcal A}(X)
 -\epsilon_2{\bf1}_{\mathcal B}(X).
\tag{3.7}
\]

The four classes have owner sizes \(16,16,16,32\). This proves the lower
ledger (0.4). Complementation proves the shifted upper ledger.

## 4. Common phase and long-cycle packing

Order

\[
 y_0=uw,\quad y_1=vw,\quad y_2=vx,\quad y_3=ux.
\]

Define \(g:\binom{[6]}3\to\mathbb Z_4\) by

\[
\begin{array}{c|rrrrrrrr}
X&125&235&345&145&126&236&346&146\\ \hline
g(X)&0&3&2&1&0&1&2&3
\end{array}
\tag{4.1}
\]

\[
\begin{array}{c|rrrrrrrr}
X&246&136&134&156&135&234&245&256\\ \hline
g(X)&1&3&0&2&1&0&3&2,
\end{array}
\tag{4.2}
\]

and put \(g(123)=g(124)=g(356)=g(456)=0\). Colour owners by

\[
                         c(X\cup y_k)=g(X)+k\pmod4.
\tag{4.3}
\]

Every square in all four factors receives \(0,1,2,3\) cyclically, up to
rotation and reversal. Adjoining \(h-2\) split pairs and using direction
word

\[
 \alpha,\beta,e_1,\ldots,e_{h-2},
 \alpha,\beta,e_1,\ldots,e_{h-2}
\tag{4.4}
\]

therefore suspends all four factors to twenty physical \(C_{2h}\)'s on
identical support.

For the global packing, reserve \(B=\lfloor m/10\rfloor\) ten-blocks and
\(P=\lfloor m/2\rfloor\) spectator pairs in disjoint coordinate regions.
The eligibility probabilities are \(5/64\) and \(1/2\). Choose each
owner's first \(r\) eligible blocks and first \(s\) split spectator pairs.
The selectors are stable under variation in

\[
                         \mathcal U^r\square Q_s.
\tag{4.5}
\]

If

\[
 r\le\frac{5B}{128},\qquad
 s\le\frac P4,\qquad
 h=2r+s=2^a,
\tag{4.6}
\]

then Chernoff and rank conditioning retain

\[
 G\ge W\left\{1-2(m+1)
 \left[e^{-5B/512}+e^{-P/16}\right]\right\}
 =W-e^{-\Omega(m)}W.
\tag{4.7}
\]

Every packet has \(4^r\) resolutions, each partitioned into \(20^r\)
copies of \(Q_h\), hence into physical \(C_{2h}\)'s. The total component
count is exactly \(G/(2h)\).

This proves positive-density cross-type action, integrality, and long
cycles simultaneously.

## 5. Induced operator and the sharp residual gate

Under the uniform owner measure, (3.7) gives

\[
\begin{array}{c|c}
\text{source type zero}&2/5\\
\text{first-bit death}&1/5\\
\text{second-bit death}&1/5\\
\text{surviving source type one}&1/5.
\end{array}
\tag{5.1}
\]

Thus corner \(11\) erases \(B\sim{\rm Bernoulli}(2/5)\). For \(L\)
product-transversal visible gadgets,

\[
 D_L\sim{\rm Bin}(L,2/5),\qquad
 \mathbb ED_L=2L/5,\qquad
 {\rm Var}(D_L)=6L/25.
\tag{5.2}
\]

Equating its mean to (1.4) gives (0.6), whose increments are

\[
 L^*_{\varepsilon,q+1}-L^*_{\varepsilon,q}
 =\frac{5(m-\varepsilon-q-1)}{2(2m-1)}
 =\frac54+O_A(m^{-1/2}).
\tag{5.3}
\]

After nested integer rounding, the maximal centred erased-binomial
fluctuation through \(q\le A\sqrt m\) is \(O_p(m^{1/4})\), hence
negligible on the \(\sqrt m\) type scale. An ideal \(5/4\)-visibility
schedule therefore has no Gaussian full-pair-type obstruction.

The proved disjoint tensor has at most \(L=q\). Its exact centre gap is

\[
 \Delta_{\varepsilon,q}-\frac{2q}{5}
 =\frac{q(2m-10\varepsilon-5q-1)}
        {10(2m-1)}
 =\frac q{10}+O_A(1).
\tag{5.4}
\]

For \(q=A\sqrt m+o(\sqrt m)\), the symmetric product total-variation gap
is

\[
                         2\Phi(A/5)-1>0.
\tag{5.5}
\]

The two-seed completion therefore improves the required overlap
multiplicity from \(3/2\) to \(5/4\), but the direct tensor still fails
the target type law.

## 6. Seams and exact implication boundary

For any fixed-frame pair-geodesic \(C_{2h}\) row at matching-switch
distance at most \(t\) from the base frame,

\[
 \mathsf W_1(\nu_{q,G},V_G)
 \le\frac{2tq}{h}G.
\tag{6.1}
\]

At \(q=A\sqrt m\), \(o(W)\) holes require
\(\Omega_A(W\sqrt m)\) pair-type transport, so such rows need
\(t/h=\Omega_A(1)\).

The standard realization cuts every component and discards its
depth-\(H\) collar, costing \(O(HW/h)\). With
\(t,H=\Theta(\sqrt m)\), this certified architecture cannot simultaneously
keep \(t/h\) positive and make \(H/h=o(1)\). This is not a universal seam
lower bound: aligned seam windows or nontrivial frame monodromy remain
outside (6.1).

Proved:

1. the exact coherent target deletion operator;
2. the exact unbiased recoupling chain and its \(\Theta(m)\) relaxation;
3. the one-seed \(1/3\) ceiling;
4. the explicit \(80\)-owner four-corner factor with affine two-sided
   signed action;
5. common all-length phase-compatible suspension;
6. near-spanning integral tensor packing with long components;
7. the exact \(2/5\) operator and \(5/4\) visibility threshold; and
8. failure of the direct tensor by the residual \(q/10\) centre gap.

Not proved:

* a physical schedule exposing \(5q/4+O_A(1)\) gadgets by depth \(q\);
* a further retile removing half of the surviving \(1/5\) high class;
* exact finite equality, rather than Gaussian-limit agreement, with every
  target type law;
* all-depth labelled target balance and cross-packet collision control;
* one common lower/upper Johnson chronology beyond the local ledgers; or
* an \(o(W)\)-seam fused braid.

Therefore the requested macroscopic transport exists, but the direct
tensor does not mix to every \(q\)-target law. The precise remaining theorem
is a \(5/4\)-visibility, all-depth, seam-aligned completion.

## 7. Detailed reports and independent audits

The detailed proofs and audits are:

* MATH_THEOREM_Q2_ASSOCIATOR_BIRTH_DEATH_AND_THREE_HALVES_GATE_20260726.md;
* MATH_AUDIT_K_Q2_GAUSSIAN_BIRTH_DEATH_TRANSPORT_20260726.md;
* MATH_ATTACK_K_Q2_ASSOCIATOR_PACKING_AND_LONG_CYCLE_CEILING_20260726.md;
* MATH_AUDIT_K_Q2_ASSOCIATOR_PACKING_LONG_CYCLE_CEILING_20260726.md;
* MATH_OBSTRUCTION_K_TWO_SEED_Q2_COMMON_CARRIER_20260726.md;
* MATH_AUDIT_K_TWO_SEED_Q2_COMMON_CARRIER_20260726.md;
* MATH_ATTACK_K_Q2_OVERLAPPING_TWO_SEED_COMPLETION_20260726.md; and
* MATH_AUDIT_K_Q2_OVERLAPPING_TWO_SEED_POSITIVE_ADDENDUM_20260726.md.
