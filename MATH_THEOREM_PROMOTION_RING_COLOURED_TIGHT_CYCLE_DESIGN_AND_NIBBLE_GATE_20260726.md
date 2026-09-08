# Promotion rings at the tuned height: the coloured tight-cycle design and the nibble gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
\lambda_q=\frac{W}{N_q}.
\]

Use the covering-side tuned height: \(H\) is the greatest integer for
which

\[
\lambda_H\le M:=m+H,
\qquad s:=m-H.                                            \tag{0.1}
\]

Then

\[
H=(1+o(1))\sqrt{m\log m},\qquad
N_H=(1+o(1))\frac Wm,                                    \tag{0.2}
\]

and, with

\[
L:=MN_H,\qquad \alpha:=\frac LW=\frac{M}{\lambda_H},
\]

\[
1\le\alpha=1+O(H/m),\qquad
L-W=O(WH/m)=o(W).                                        \tag{0.3}
\]

For every carrier \(A\in\binom{[2m]}s\), put
\(U=[2m]\setminus A\), so \(|U|=M\). A cyclic order of \(U\) selects

\[
Y_j=A\cup I_\pi(j,H),\qquad j\in\mathbb Z_M,              \tag{0.4}
\]

where the \(I_\pi(j,H)\) form a tight Hamilton cycle in the complete
\(H\)-uniform hypergraph on \(U\).

The exact outcome is as follows.

1. The middle carrier--cycle hypergraph has a completely symmetric
   fractional design. Giving every frame through a carrier weight
   \(1/(M-1)!\) loads every carrier by one and every middle target by
   \(\alpha=1+o(1)\). Giving every frame weight \(1/D\), where

   \[
   D=\frac{(m!)^2}{(m-H)!},                                \tag{0.5}
   \]

   loads every middle target by one and every carrier by
   \(1/\alpha=1-O(H/m)\). Thus discarding only
   \(O((L-W)/M)=o(N_H)\) carriers removes the scalar excess.

2. The middle codegrees are exact. If two middle targets have Johnson
   distance \(d\), then for \(1\le d<H\)

   \[
   \frac{D(Y,Z)}D=\frac{2}{\binom md^2},                   \tag{0.6}
   \]

   at \(d=H\)

   \[
   \frac{D(Y,Z)}D=\frac{m-H+1}{\binom mH^2},               \tag{0.7}
   \]

   and for \(d>H\) the codegree is zero. Hence

   \[
   \frac{\Delta_2}{D}=\frac2{m^2}.                         \tag{0.8}
   \]

   The exact conditioned overlap of one frame is much smaller than the
   worst-pair reduction: for every middle vertex \(Y\) of a frame,

   \[
   \frac1D\sum_{\substack{Z\text{ in the frame}\\Z\ne Y}}D(Y,Z)
   =\frac4{m^2}+O(m^{-4})
     +\exp[-\Theta(H\log(m/H))],                            \tag{0.9}
   \]

   and the whole frame has normalized unordered overlap

   \[
   \frac1D\sum_{\{Y,Z\}\text{ in the frame}}D(Y,Z)
   =\frac2m+O(m^{-2}).                                     \tag{0.10}
   \]

3. These parameters make a fresh isolated nibble bite efficient, but
   the available growing-uniformity theorems do not yield the needed
   factor. With edge size \(k=M+1\) and vertex census \(V=W+N_H\),

   \[
   \frac{k\Delta_2\log V}{D_{\min}}
   =4\log2+o(1),                                           \tag{0.11}
   \]

   whereas the variable-rank criterion requires this quantity to tend
   to zero. The more recent full-codegree theorem also does not
   diagonalize: its bottleneck is at most
   \(\sqrt{D/\Delta_2}=(1+o(1))m/\sqrt2\), while its published
   polylogarithmic hierarchy requires a power of
   \(\log D=\Theta(m\log m)\) far exceeding \(m\).

4. A hypothetical group-respecting middle matching leaving \(o(W)\)
   middle targets would be quantitatively sufficient. It would use
   \(W/M-o(W/m)\) distinct carriers; restoring all omitted carriers
   creates only \(o(W)\) additional middle collisions. Thus the
   obstruction is not a stronger absolute leave requirement at the
   middle rank. It is the absence of a diagonal cycle-factor theorem.

5. The all-rank problem is genuinely stronger. The tag census has an
   exact fractional solution with load one on every target at every
   controlled rank, but the total coloured target census is

   \[
   W+2\sum_{q=1}^{H}N_q
   =(\sqrt\pi+o(1))W\sqrt m.                               \tag{0.12}
   \]

   Consequently an ordinary relative \(o(1)\) coloured leave is
   insufficient; its relative error must be \(o(m^{-1/2})\).
   Moreover adjacent nested colours have relative codegree
   \(\Theta(m^{-1})\), and the effective decorated-ring size is
   \((\sqrt\pi+o(1))m^{3/2}\). A naive all-rank matching theorem sees
   codegree times edge size of order \(\sqrt m\).

6. Independent or product-nibble frame choices have
   \(\Theta(W)\) floor energy at each of \(\Theta(\sqrt m)\) Gaussian
   ranks, hence \(\Theta(W\sqrt m)\) in aggregate. Therefore current
   cycle-nibble methods, even if they were upgraded to settle the middle
   matching, do not by themselves attain the required absolute \(o(W)\)
   all-rank defect. The missing result is a coloured/resolvable
   tight-cycle selection producing cross-carrier negative dependence
   simultaneously for all nested window lengths.

The note proves no nonexistence theorem for a globally correlated
promotion-ring resolution. It proves exact fractional feasibility,
exact local coefficients, and a sharp no-go for applying current
cycle-nibble statements as black boxes.

## 1. The tuned census and the middle normal form

The ratio recurrence

\[
\frac{\lambda_{q+1}}{\lambda_q}
=\frac{m+q+1}{m-q}                                       \tag{1.1}
\]

and maximality in (0.1) give

\[
1\le\frac{M}{\lambda_H}
<\frac{M}{m-H}=1+O(H/m).                                 \tag{1.2}
\]

Together with

\[
\log\lambda_q
=\frac{q(q+1)}m+O(q^3/m^2+q/m),                          \tag{1.3}
\]

this proves (0.2)--(0.3).

Fix \(A\in\binom{[2m]}s\) and \(U=A^c\). Let
\(\mathcal C_A\) be the directed cyclic orders of \(U\), modulo
rotation. Thus

\[
|\mathcal C_A|=F:=(M-1)!.                                \tag{1.4}
\]

For \(\pi\in\mathcal C_A\), the \(H\)-sets
\[
I_\pi(0,H),I_\pi(1,H),\ldots,I_\pi(M-1,H)
\]
are the edges of a tight Hamilton cycle in \(K_U^{(H)}\). Equation
(0.4) maps them bijectively to \(M\) middle owners containing \(A\).

Let \(\mathcal G\) be the \((M+1)\)-uniform hypergraph with

* one left vertex for every carrier \(A\);
* one right vertex for every \(Y\in\binom{[2m]}m\); and
* one edge \((A,\pi)\) consisting of \(A\) and the \(M\) owners (0.4).

A matching in \(\mathcal G\) is exactly a collection of distinct
carriers with pairwise owner-disjoint tight cycles.

## 2. Exact degrees and the two fractional designs

### Proposition 2.1 (degrees)

Every carrier has degree \(F=(M-1)!\). Every middle target has degree

\[
\boxed{
D=\binom mH H!m!
=\frac{(m!)^2}{s!}.}                                      \tag{2.1}
\]

Moreover

\[
\frac FD=\frac{\lambda_H}{M}=\frac1\alpha
=1-O(H/m).                                                \tag{2.2}
\]

#### Proof

The carrier degree is immediate. Fix a middle target \(Y\). A carrier
which can generate \(Y\) is an \(s\)-subset \(A\subset Y\), so there
are \(\binom mH\) choices. For such \(A\), the set
\(I=Y\setminus A\) has size \(H\). Contracting \(I\) to one cyclic block
shows that exactly \(H!m!\) directed cyclic orders of \(U=A^c\) contain
\(I\) as a window. This proves (2.1).

Finally

\[
\frac FD
=\frac{(M-1)!s!}{(m!)^2}
=\frac1M\frac{s!M!}{(m!)^2}
=\frac{\lambda_H}{M}.
\]
\(\square\)

### Corollary 2.2 (exact fractional points)

There are two useful uniform fractional selections.

* Weight \(x_{A,\pi}=1/F\) gives every carrier load one, every middle
  target load \(D/F=\alpha\), and total selected edge mass \(N_H\).
* Weight \(x_{A,\pi}=1/D\) gives every middle target load one, every
  carrier load \(F/D=1/\alpha\), and total selected edge mass \(W/M\).

Thus the exact fractional carrier deficit in the right-perfect point is

\[
N_H-\frac WM=\frac{L-W}{M}=O(WH/m^2)=o(N_H).               \tag{2.3}
\]

The adjacent convention—take the least \(H\) with
\(\lambda_H\ge m+H\)—reverses the inequalities: one frame per carrier
has middle load \(1-O(H/m)\) and misses only \(o(W)\) owners. All local
degree and codegree formulae are unchanged.

## 3. Exact middle codegrees

Fix distinct \(Y,Z\in\binom{[2m]}m\), and write

\[
d=|Y\setminus Z|=|Z\setminus Y|.
\]

### Theorem 3.1 (right-pair codegrees)

For \(1\le d<H\),

\[
\boxed{
D(Y,Z)=\frac{2(d!)^2(m-d)!^2}{s!},\qquad
\frac{D(Y,Z)}D=\frac2{\binom md^2}.}                       \tag{3.1}
\]

For \(d=H\),

\[
\boxed{
D(Y,Z)=(H!)^2(s+1)!,\qquad
\frac{D(Y,Z)}D=\frac{s+1}{\binom mH^2}.}                   \tag{3.2}
\]

For \(d>H\), \(D(Y,Z)=0\). Consequently (0.8) holds.

#### Proof

A common carrier must be an \(s\)-subset of \(Y\cap Z\). For \(d<H\)
there are

\[
\binom{m-d}{s}=\binom{m-d}{H-d}
\]

choices. Once \(A\) is fixed, \(Y\setminus A\) and \(Z\setminus A\)
are two \(H\)-sets at distance \(d\) in \(U=A^c\). For both to be
cyclic windows, their four Venn cells must occur as four consecutive
blocks. The directed count is

\[
2(d!)^2(H-d)!(m-d)!.
\]

Multiplication and cancellation give (3.1).

If \(d=H\), the common carrier is \(A=Y\cap Z\), and the two
\(H\)-sets are disjoint. Contracting them to two cyclic blocks gives
\((H!)^2(M-2H+1)!=(H!)^2(s+1)!\) orders. If \(d>H\), the intersection
has size below \(s\), so no common carrier exists. The maximum normalized
value is the \(d=1\) term. \(\square\)

### Proposition 3.2 (carrier--target codegree)

For \(A\subset Y\), \(|A|=s\),

\[
D(A,Y)=H!m!,                                             \tag{3.3}
\]

and otherwise it is zero. Hence

\[
\frac{D(A,Y)}D=\frac1{\binom mH},\qquad
\frac{D(A,Y)}F=\frac{M}{\binom MH}.                       \tag{3.4}
\]

Both ratios are superpolynomially smaller than \(m^{-2}\).

### Proposition 3.3 (conditioned interval overlap)

Fix one frame edge \(e=(A,\pi)\) and \(Y\in e\) on the middle shore.
Then

\[
\begin{aligned}
\frac1D\sum_{Z\in e\setminus\{Y\}}D(Y,Z)
={}&4\sum_{d=1}^{H-1}\binom md^{-2}
  +\frac{(s+1)^2}{\binom mH^2}                             \tag{3.5}\\
={}&\frac4{m^2}+O(m^{-4})
  +\exp[-\Theta(H\log(m/H))].
\end{aligned}
\]

Consequently

\[
\frac1D\sum_{\{Y,Z\}\subset e}D(Y,Z)
=\frac M2\left(\frac4{m^2}+O(m^{-4})+e^{-\Theta(H\log(m/H))}\right)
=\frac2m+O(m^{-2}).                                      \tag{3.6}
\]

#### Proof

Relative to one cyclic \(H\)-window, a frame has exactly two other
windows at every Johnson distance \(1\le d<H\), and exactly
\(M-2H+1=s+1\) disjoint \(H\)-windows. Insert (3.1)--(3.2). The
\(d=1\) term dominates; log-concavity bounds all \(d\ge2\) terms as
displayed. Sum over \(Y\) and divide by two for unordered pairs.
\(\square\)

The top--right pairs add only
\(M/\binom mH\) to the normalized edge overlap, so they do not change
(3.6).

### Remark 3.4 (all codegrees)

There is also an exact finite reduction for every higher codegree. For
distinct middle targets \(Y_1,\ldots,Y_j\),

\[
D(Y_1,\ldots,Y_j)
=\sum_{\substack{A\subseteq\cap_iY_i\\|A|=s}}
c_{A^c}(Y_1\setminus A,\ldots,Y_j\setminus A),             \tag{3.7}
\]

where \(c_U(I_1,\ldots,I_j)\) is the number of cyclic orders of \(U\)
in which all \(I_i\) are \(H\)-windows. If

\[
a_J=\#\{u\in U:\{i:u\in I_i\}=J\},
\]

and, for a start vector \(t=(0,t_2,\ldots,t_j)\), put

\[
c_J(t)=\#\{z\in\mathbb Z_M:
              \{i:z\in[t_i,t_i+H)\}=J\}.
\]

then the directed breakpoint formula is

\[
c_U(I_1,\ldots,I_j)
=
\sum_{\substack{t_1=0,\ t_2,\ldots,t_j\ {\rm distinct}\\
                 c_J(t)=a_J\ \forall J}}
\prod_{J\subseteq[j]}a_J!.                                \tag{3.8}
\]

Thus no higher-codegree datum is formally missing; what is missing is a
uniform diagonal rounding theorem.

## 4. Exact audit of cycle-nibble methods

The augmented hypergraph \(\mathcal G\) is asymptotically regular:
its left and right degrees differ by \(1+O(H/m)\), and its maximum
pair codegree relative to the smaller degree is

\[
\frac{\Delta_2}{D_{\min}}=\frac{2+o(1)}{m^2}.               \tag{4.1}
\]

Its edge size is \(k=M+1=(1+o(1))m\), while

\[
\log(W+N_H)=2m\log2+O(\log m).
\]

Therefore

\[
\boxed{
\frac{k\Delta_2\log(W+N_H)}{D_{\min}}
=4\log2+o(1).}                                            \tag{4.2}
\]

The variable-rank Grable criterion requires the left side to be \(o(1)\).
Thus the promotion-ring middle design lies at its constant boundary, not
inside its range.

The full-codegree bottleneck used by the newer nibble is at most

\[
\mathfrak B
\le\sqrt{\frac{D_{\min}}{\Delta_2}}
=(1+o(1))\frac m{\sqrt2}.                                 \tag{4.3}
\]

But \(\log D_{\min}=\Theta(m\log m)\). The published fixed-uniformity
hierarchy requires a polylogarithmic power exceeding \(\mathfrak B\)
when \(k\to\infty\); in its explicit form it asks for a condition of the
shape

\[
\mathfrak B\ge(\log D_{\min})^{10/\gamma^4},
\qquad \gamma\ll1/k,
\]

which is impossible here. Hence that theorem cannot be diagonalized to
this family even if (3.7)--(3.8) have their optimal conceivable values.

On the positive side, (3.6) is \(o(1)\). It proves that one isolated
random bite has small internal collision correction; replacing every
pair in an edge by the worst codegree loses a factor \(m\). What is not
proved is hereditary regeneration of the group-respecting residual.

### Proposition 4.1 (the middle leave required is only \(o(W)\))

Suppose a matching in \(\mathcal G\) covers \(W-o(W)\) right vertices.
Then it uses

\[
\frac WM-o(W/m)
\]

distinct carriers. Restoring an arbitrary frame on every omitted carrier
creates only \(o(W)+(L-W)=o(W)\) additional middle collision mass.

#### Proof

Every matching edge contains exactly \(M\) right vertices. Thus a
matching covering \(W-o(W)\) of them has \(W/M-o(W/m)\) edges and hence
that many distinct carriers. There are \(N_H=L/M=W/M+(L-W)/M\)
carriers. The number omitted is therefore

\[
o(W/m)+\frac{L-W}{M}=o(W/m).
\]

Each restored frame contributes \(M\) occurrences, so their total
possible collision contribution is \(o(W)\). \(\square\)

Accordingly, an applicable near-perfect matching theorem with ordinary
absolute \(o(W)\) leave would settle the middle normal form. Current
cycle-nibble theorems do not provide it in this diagonal.

## 5. Nested colours and exact fractional balance

For a packet \((U,\pi)\), every rank \(r\), \(s\le r<M\), has \(M\)
cyclic \(r\)-intervals. A fixed \(r\)-target has packet degree

\[
\boxed{
d_r=\binom{2m-r}{M-r}r!(M-r)!
=\frac{r!(2m-r)!}{s!}.}                                   \tag{5.1}
\]

In particular, for \(0\le q<H\),

\[
d_{m-q}=d_{m+q}=\lambda_qD.                               \tag{5.2}
\]

At \(q=H\), the lower identity \(d_s=\lambda_HD=M!\) remains
valid. The upper target is the carrier top \(U\) itself and is handled
by its marker of degree \(F=(M-1)!\).

If \(S\subset T\), \(|S|=r\), and \(|T|=r+1\), direct endpoint
counting gives

\[
d(S,T)=\frac{2r!(2m-r-1)!}{s!},                           \tag{5.3}
\]

so

\[
\frac{d(S,T)}{d_r}=\frac2{2m-r},\qquad
\frac{d(S,T)}{d_{r+1}}=\frac2{r+1}.                       \tag{5.4}
\]

Both are \(\Theta(m^{-1})\) throughout the controlled band. These are
the nested-window threads.

For completeness, the same-rank coefficient retains the favorable
scale. Whenever two \(r\)-targets at distance \(d\) fit in a common top,

\[
\frac{d_r(S,T)}{d_r}
=\frac{2}{\binom rd\binom{2m-r}d}                         \tag{5.5}
\]

in the overlapping case, with the usual disjoint endpoint formula.
Thus its maximum is \((2+o(1))/m^2\).

Now use the exact SCD tag census

\[
g_d=N_d-N_{d+1}\quad(0\le d<H),\qquad g_H=N_H,            \tag{5.6}
\]

together with \(L-W\) vacancies. These counts fill the \(L=MN_H\)
ring phases, and

\[
\sum_{d=q}^{H}g_d=N_q.                                    \tag{5.7}
\]

There is an exact fractional all-rank design:

* choose the cyclic frame of every carrier uniformly;
* assign the tag census fractionally and symmetrically to the \(L\)
  phase slots, with one tag \(H\) per carrier in the carrier marginal.

At signed depth \(q\), a uniform frame makes the raw phase map uniform
over the \(N_q\) targets. There are \(L\) raw slots and exactly \(N_q\)
active slots. Hence every target has fractional load

\[
\frac{L}{N_q}\cdot\frac{N_q}{L}=1.                        \tag{5.8}
\]

This is an exact linear construction, not an inference from unrelated
marginal estimates. It proves fractional feasibility of the decorated
carrier-cycle system.

## 6. Why the nested problem needs more than a cycle factor

Since \(H/\sqrt m\to\infty\), Gaussian summation gives

\[
\sum_{q=0}^{H}N_q
=\left(\frac{\sqrt\pi}{2}+o(1)\right)W\sqrt m.             \tag{6.1}
\]

Counting both signed ranks, with the middle only once, gives (0.12).
The mean number of target cells carried by one selected tagged ring is
therefore

\[
\frac{W+2\sum_{q=1}^{H}N_q}{N_H}
=(\sqrt\pi+o(1))m^{3/2}.                                  \tag{6.2}
\]

Consequently:

* a generic relative leave \(\varepsilon_m\) on the coloured target
  union gives absolute defect
  \((\sqrt\pi+o(1))\varepsilon_mW\sqrt m\);
* obtaining \(o(W)\) requires
  \(\varepsilon_m=o(m^{-1/2})\);
* inserting all target cells as ordinary vertices produces effective
  edge size \(\Theta(m^{3/2})\), while (5.4) gives relative adjacent
  codegree \(\Theta(m^{-1})\).

Thus a naive all-colour matching theorem is farther outside the usual
nibble range than the middle problem. The nested paths must be contracted
and treated as compulsory coloured threads.

There is also a direct product-law obstruction. Fix a Gaussian interval
\(a\sqrt m\le q\le b\sqrt m\), \(0<a<b<\infty\), and independently
choose the cyclic frames in different carriers. For a target \(T\), let
\(Z_{q,T}\) be its load after the exact threshold-\(q\) tag census.
Then

\[
\sum_TZ_{q,T}=N_q,
\qquad
Q_q:=\sum_T(Z_{q,T}-1)^2
=\sum_TZ_{q,T}(Z_{q,T}-1).                                \tag{6.3}
\]

Write \(Z_{q,T}=\sum_A X_{A,T}\), where a fixed carrier contributes at
most one copy of \(T\) at that rank. Under independent frames,

\[
\sum_T\operatorname{Var}Z_{q,T}
=\sum_{A,T}p_{A,T}(1-p_{A,T}).                             \tag{6.4}
\]

The first-moment sum is \(N_q\). Uniformly in the displayed Gaussian
interval, the largest \(p_{A,T}\) is
\(\exp[-\Theta(H\log(m/H))]\), because a prescribed interval of length
\(H\pm q\) must occur in a cyclic order of \(M\) labels. Hence

\[
\sum_T\operatorname{Var}Z_{q,T}
=(1-o(1))N_q=\Theta_{a,b}(W).                              \tag{6.5}
\]

Since

\[
\mathbb E Q_q
=\sum_T(\mathbb EZ_{q,T}-1)^2
 +\sum_T\operatorname{Var}Z_{q,T},                        \tag{6.6}
\]

every such rank has expected floor energy \(\Theta(W)\). Summing over
\(\Theta(\sqrt m)\) Gaussian ranks yields

\[
\sum_{a\sqrt m\le q\le b\sqrt m}\mathbb E Q_q
=\Theta_{a,b}(W\sqrt m).                                  \tag{6.7}
\]

Thus independent ring heat and a product-style nibble converge to the
wrong all-rank scale. A successful selection must create negative
cross-carrier covariance of order \(W\sqrt m\), while retaining the
middle tight-cycle packing.

## 7. Exact remaining theorem

The promotion-ring programme reduces to the following coloured,
resolvable tight-cycle statement.

> Choose one cyclic \(H\)-window cycle in every carrier \(U\), together
> with the exact nested tag census, so that:
>
> 1. middle loads are one except for \(o(W)\) total collision/leave;
> 2. at every shorter and longer window length, the floor-correct
>    aggregate hole energy summed over all ranks is \(o(W)\); and
> 3. the one-tag-\(H\)-per-carrier and promotion-path constraints are
>    preserved.

The exact fractional solution is (2.1)--(2.3) and (5.6)--(5.8). The
exact pair and thread kernels are (3.1)--(3.6) and (5.3)--(5.5).

For the middle-only problem, an \(o(W)\)-leave group-respecting cycle
matching would suffice, but no current growing-uniformity cycle-nibble
theorem applies. For the all-rank problem, even such a middle factor is
not enough: the required coloured leave rate is \(o(m^{-1/2})\), and
product/quasirandom choices have \(\Theta(W\sqrt m)\) floor energy.

No scalar, fractional, or pair-codegree obstruction remains. The missing
object is a globally correlated coloured resolution, not an ordinary
tight-cycle near-factor.

## References used for the nibble comparison

* S. Gould and T. Kelly, *Advancing the Rödl Nibble: New bounds on
  matchings and the list chromatic index of hypergraphs*,
  arXiv:2511.11375, especially Theorem 1.4.
* The Grable/Kostochka--Rödl variable-rank criterion in the normalization
  reviewed in the preceding fixed-annulus packet notes.
