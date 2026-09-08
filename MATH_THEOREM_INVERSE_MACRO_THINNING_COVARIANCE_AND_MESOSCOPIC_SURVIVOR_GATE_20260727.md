# Inverse macro thinning: controlled endpoint kernel, retained factorial covariance, and the mesoscopic survivor gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let \(\mathcal H^\square\) be the simple domino-twin catalogue, with

\[
 n=2m,\qquad K=4m,\qquad
 D=2^{1-m}R!(n-R)!,
\tag{0.1}
\]

and

\[
 \log D=2m\log m-(2+\log2)m+O_a(\log m).
\tag{0.2}
\]

Assume the proposed sharp inverse estimate with exponent
\(\chi<1/2\): for some fixed \(C_I\), every simple packet \(F\) and
every \(1\le u\le m\) satisfy

\[
 \boxed{
 M_F(u):=
 |\{G:|F\cap G|\ge K-u\}|
 \le e^{C_Im}m^{\chi u}.}
\tag{INV\(_\chi\)}
\]

Put \(\delta=1/2-\chi>0\), choose

\[
 s=\left\lceil {A m\over\log m}\right\rceil
\tag{0.3}
\]

with \(A\) sufficiently large in terms of \(\delta,C_I\), and perform
the macro-overlap conflict thinning at deficit \(s\).

The rigorous conclusions are:

1. The retained simple catalogue has degree

   \[
    D_s=(1+o(1)){D\over\Delta_s+1},
    \qquad
    \Delta_s\le e^{C_Im}m^{\chi s},
   \tag{0.4}
   \]

   retains the original \(O(m^{-2})\) relative pair-codegree scale, and
   contains no pair with overlap \(>K-s\).

2. At a square-root density

   \[
                         z={C_\star\over\sqrt m},
   \tag{0.5}
   \]

   the entire retained **macro sector**

   \[
                         |F\cap G|\ge K-m
   \tag{0.6}
   \]

   has incidence-averaged survivor kernel \(e^{-\Omega(m)}\), provided
   \(A\) is large enough. The factor \(m^{\chi u}\) is beaten exactly by
   \(m^{u/2}\).

3. The same conflict thinning preserves, incidence-averaged, every
   logarithmic factorial covariance:

   \[
    {\sum_X\sum_{\substack{F,G\in L_s(X)\\F\ne G}}
          (|F\cap G|-1)_p
     \over
     \sum_X d_s(X)(d_s(X)-1)}
    \le (Cp)^{Cp}m^{-2+o(1)}
   \tag{0.7}
   \]

   uniformly for \(1\le p\le C_0\log m\).

4. The literal unit-constant density \(z=m^{-1/2}\) is already
   below the simple-catalogue degree threshold:

   \[
                         Dz^{K-1}=e^{-(2+\log2+o(1))m}.
   \tag{0.8}
   \]

   Conflict thinning only decreases it. A slow-bite degree corridor can
   therefore target \(C_\star m^{-1/2}\) only with a sufficiently large
   constant \(C_\star\). This still gives leave \(O(N/\sqrt m)\).

5. Even after correcting that constant, (INV\(_\chi\)) and all the
   logarithmic factorial bounds do **not** control the full survivor
   kernel. They leave the mesoscopic sector

   \[
                  C_0\log m\ll |F\cap G|-1<K-m
   \tag{0.9}
   \]

   completely open. An explicit abstract overlap law supported at
   \(j=\lfloor\sqrt m\rfloor\) satisfies every assumed logarithmic moment
   and has no macro mass, yet its survivor kernel at (0.5) diverges like

   \[
      \exp\!\left[(1/2+o(1))\sqrt m\log m\right].
   \tag{0.10}
   \]

6. The exact stopped covariance generator still has no sign. Macro
   thinning controls its largest possible jumps and (0.7) controls its
   entrance-time logarithmic diagrams, but neither statement implies the
   current-residual column moments or the integrated stratum-hazard
   estimate.

Thus the assumed exponent \(\chi<1/2\) closes the macroscopic endpoint
of the survivor problem. It does not prove stopped regeneration to the
square-root scale. The next exact failure is the **mesoscopic survivor
kernel**, followed by its current-residual common-column covariance.

## 1. A joint-retention lemma for conflict thinning

Let \(\Gamma\) be a \(\Delta\)-regular graph. Give its vertices
independent uniform priorities and retain a vertex precisely when it is
the unique minimum in its closed neighbourhood. Put

\[
                         \rho={1\over\Delta+1}.
\tag{1.1}
\]

Adjacent vertices are never both retained.

### Lemma 1.1

For two distinct nonadjacent vertices \(F,G\),

\[
 \boxed{\Pr(F,G\text{ both retained})\le2\rho^2.}
\tag{1.2}
\]

Consequently

\[
 \Pr(G\text{ retained}\mid F\text{ retained})\le2\rho.
\tag{1.3}
\]

#### Proof

Let \(a\) be the number of common neighbours of \(F,G\). Conditional on
their priorities being \(x\le y\), the exclusive neighbours of \(F\)
must exceed \(x\), while the exclusive neighbours of \(G\) and all common
neighbours must exceed \(y\). Therefore

\[
\begin{aligned}
 \Pr(F,G\text{ retained})
 &=2\int_0^1(1-y)^\Delta
       \int_0^y(1-x)^{\Delta-a}\,dx\,dy\\
 &\le2\int_0^1y(1-y)^\Delta\,dy\\
 &=\frac2{(\Delta+1)(\Delta+2)}
 \le2\rho^2.
\end{aligned}
\tag{1.4}
\]

Division by \(\Pr(F\text{ retained})=\rho\) proves (1.3).
\(\square\)

This elementary inequality is the cancellation needed below: after
normalization by \(D_s=\rho D\), the conflict-thinning cost does not appear a
second time in a retained pair profile.

## 2. The macro survivor kernel closes under \(\chi<1/2\)

For a retained incidence \(X\in F\), define its macro survivor kernel by

\[
 \mathcal K^{\rm mac}_{X,F}(z)
 ={1\over D_s}
 \sum_{\substack{G\in L_s(X),\,G\ne F\\
                  |F\cap G|\ge K-m}}
 z^{-(|F\cap G|-1)}.
\tag{2.1}
\]

We first estimate its incidence average over the random priority
thinning. If \(u=K-|F\cap G|\), then retained pairs have \(u\ge s\).
Lemma 1.1 and \(D_s=\rho D\) give

\[
\begin{aligned}
 \mathbb E\!\left[
  {\bf1}_{\{F\ {\rm retained}\}}
  \mathcal K^{\rm mac}_{X,F}(z)\right]
 &\le {2\rho^2\over \rho D}
 \sum_{u=s}^{m}M_F(u)z^{-(K-u)}\\
 &={2\rho\over D}
 \sum_{u=s}^{m}M_F(u)z^{-(K-u)}.
\end{aligned}
\tag{2.2}
\]

After summing over \(F\ni X\), the leading factor \(\rho D=D_s\) cancels.
Thus the normalized retained-incidence expectation is at most

\[
 {2\over D}\sum_{u=s}^{m}M_F(u)z^{-(K-u)}.
\tag{2.3}
\]

Substitute (INV\(_\chi\)), (0.2), and \(z=C_\star/\sqrt m\), where
\(C_\star\ge1\). Uniformly
for \(s\le u\le m\), the logarithm of the \(u\)-summand in (2.3) is at
most

\[
 -\delta u\log m+
 \bigl(C_I+2+\log2\bigr)m+O(\log m).
\tag{2.4}
\]

Choose

\[
 A>{C_I+2+\log2+2\over\delta}.
\tag{2.5}
\]

Then (2.4) is at most \(-2m+O(\log m)\) at \(u=s\), and it decreases
geometrically with \(u\). Hence

\[
 \boxed{
 {1\over\sum_Xd_s(X)}
 \sum_X\sum_{F\in L_s(X)}
 \mathcal K^{\rm mac}_{X,F}(z)
 \le e^{-\Omega(m)}}
\tag{2.6}
\]

for some deterministic priority realization, after changing the
constant in the exponent.

To justify the last deterministic choice, first take a realization with
the simultaneous degree conclusions of the conflict-thinning theorem.
The expected numerator in (2.6) is \(e^{-\Omega(m)}\) times its
denominator. Markov's inequality at threshold \(e^{-\Omega(m)/2}\)
leaves positive probability. Thus one realization has both properties.

Equation (2.6) is incidence-averaged, which is the correct strength for
weighted quarantine. It does not assert an unnecessary pointwise bound
for every surviving packet.

## 3. Logarithmic factorial covariance survives the thinning

For \(1\le p\le C_0\log m\), put

\[
 Z_{p,X}
 =\sum_{\substack{F,G\in L_s(X)\\F\ne G}}
       (|F\cap G|-1)_p.
\tag{3.1}
\]

The static simple-catalogue theorem gives, for each \(X\) and \(F\ni X\),

\[
 \sum_{\substack{G\ni X\\G\ne F}}
       (|F\cap G|-1)_p
 \le (Cp)^{Cp}m^{-2}D.
\tag{3.2}
\]

Lemma 1.1 therefore yields

\[
 \mathbb EZ_{p,X}
 \le2\rho^2(Cp)^{Cp}m^{-2}D^2
 =2(Cp)^{Cp}m^{-2}D_s^2.
\tag{3.3}
\]

Here \(p\) is only the factorial order. The retention probability is
\(\rho\), and the final expression uses \(D_s=\rho D\).

Sum (3.3) over \(X\), and then sum over the \(O(\log m)\) factorial
orders. Markov's inequality with a factor \(m^{o(1)}\), intersected with
the simultaneous degree event, gives one deterministic thinned
catalogue satisfying

\[
 \sum_XZ_{p,X}
 \le(Cp)^{Cp}m^{-2+o(1)}
       \sum_Xd_s(X)(d_s(X)-1)
\tag{3.4}
\]

for every displayed \(p\). This is (0.7).

The conclusion is deliberately incidence-averaged. It permits deleting
all rows whose individual normalized factorial mass exceeds a threshold
\(b_p\), with total deleted incidence at most the right side of (3.4)
divided by \(b_p\).

## 4. The unit-constant square-root degree failure

Before any conflict thinning, the formal product-thinned simple degree is

\[
                         D_z=Dz^{K-1}.
\tag{4.1}
\]

At \(z=m^{-1/2}\), equations (0.1)--(0.2) give

\[
 \log D_z
 =-(2+\log2)m+O_a(\log m),
\tag{4.2}
\]

which proves (0.8). A reference degree tending exponentially to zero
cannot support a stopped corridor centred on that product reference. A
highly structured non-product residual is not excluded by this
arithmetic, but it would require a different comparison trajectory.

At \(z=C_\star/\sqrt m\), after conflict thinning,

\[
 \log(D_sz^{K-1})
 \ge
 \bigl(4\log C_\star-2-\log2-C_I-\chi A-o(1)\bigr)m.
\tag{4.3}
\]

Thus choose

\[
 4\log C_\star>2+\log2+C_I+\chi A+1.
\tag{4.4}
\]

Then the retained reference degree is exponential throughout the stop.
The resulting entrance leave is still \(O(N/\sqrt m)\). Hence the
unit-constant failure is a constant-factor entropy issue, not an
exponent obstruction.

## 5. The mesoscopic survivor kernel is not controlled

The macro inverse bound applies only when

\[
                         |F\cap G|\ge K-m.
\tag{5.1}
\]

The logarithmic factorial hierarchy tests powers only through
\(L=C_0\log m\). Between these ranges lies

\[
                         L<j:=|F\cap G|-1<K-m-1.
\tag{5.2}
\]

Neither (INV\(_\chi\)) nor (3.2) controls the exponential transform
\[
                         \sum_j a_jz^{-j}.
\]

### Proposition 5.1 (literal logical separation)

There is an abstract overlap law satisfying (INV\(_\chi\)) trivially
and every logarithmic factorial inequality (3.2), but whose survivor
kernel diverges at \(z=C_\star/\sqrt m\).

#### Proof

Put \(j_0=\lfloor\sqrt m\rfloor\), \(L=C_0\log m\), and

\[
 \varepsilon_m
 =m^{-2}\min_{1\le p\le L}
       {(Cp)^{Cp}\over(j_0)_p}.
\tag{5.3}
\]

Give the normalized overlap law mass \(\varepsilon_m\) at \(j_0\) and
the remaining mass at \(0\). It has no support in the macro range (5.1),
so every macro inverse inequality holds. Also, for \(p\le L\),

\[
                         \varepsilon_m(j_0)_p
 \le(Cp)^{Cp}m^{-2}.
\tag{5.4}
\]

On the other hand,

\[
 \log\varepsilon_m=-O((\log m)^2),
\tag{5.5}
\]

while

\[
\begin{aligned}
 \log(\varepsilon_mz^{-j_0})
 &=\frac12\sqrt m\log m
   -\sqrt m\log C_\star-O((\log m)^2)\\
 &\longrightarrow+\infty.
\end{aligned}
\tag{5.6}
\]

Thus the survivor kernel is unbounded. \(\square\)

Proposition 5.1 is an obstruction to the proposed implication from the
two assumed inputs. It is not asserted to be realized by the actual
domino catalogue. Ruling it out there requires a new mesoscopic inverse
theorem, for example

\[
 \boxed{
 {1\over D}\sum_{\substack{G\ni X\\
          L<|F\cap G|-1<K-m}}
 \left({\sqrt m\over C_\star}\right)^{|F\cap G|-1}
 =o(1),}
\tag{MSK}
\]

uniformly or incidence-weightedly outside an \(o(1/K)\) quarantine.

This is the exact remaining static survivor-kernel statement.

## 6. The stopped covariance generator remains open

For the later slow bite, write

\[
 A_{p,t}(X,F)
 ={S_{p,t}(X,F)\over \bar d_t(X)}.
\]

If a selected edge \(e\) is disjoint from the protected row \(F\), the
exact stopped increment is

\[
 \boxed{
 \Delta_eA_{p,t}
 ={A_{p,t}B_X(e)-C_{p,X,F}(e)
   \over\bar d_t(X)-B_X(e)}.}
\tag{6.1}
\]

Macro thinning bounds the largest possible row overlap and (2.6) makes
the retained macro survivor mass negligible. Equation (3.4) controls
the entrance-time aggregate of the logarithmic weights. Neither controls
the sign of

\[
                         A_{p,t}B_X(e)-C_{p,X,F}(e)
\tag{6.2}
\]

in the current residual.

Equivalently, for overlap strata \(N_{j,t}\), the compensated generator
is

\[
 { \mathcal G_t
      (N_{j,t}z_t^{-(K-1-j)})
  \over N_{j,t}z_t^{-(K-1-j)}}
 =(K-1-j)h_t-h_{j,t}.
\tag{6.3}
\]

The next dynamic theorem must prove, after weighted quarantine,

\[
 \int_0^T
 |h_{j,t}-(K-1-j)h_t|\,dt=o(1)
\tag{6.4}
\]

on the mesoscopic mass relevant to (MSK), together with

\[
 \int_0^T{1\over N_{j,t}^{\ell}}
 \sum_e\nu_t(e)B_{j,t}(e)^\ell\,dt=o(1)
 \qquad(\ell=2,C_0\log m).
\tag{6.5}
\]

These are current-residual common-column estimates. Static factorial
covariance, even after macro conflict thinning, does not imply them.

There is a literal statewise reason. In the abstract law from Proposition
5.1, let one possible next-event column delete only rows in the
zero-overlap class. Then \(C_{p,X,F}(e)=0\), while
\(A_{p,t}B_X(e)>0\), so (6.1) has positive numerator. A column deleting
only the \(j_0\)-rows has the opposite sign. Both states have the same
row-overlap histogram before the event. Hence neither the macro cutoff
nor any collection of row factorial moments determines the stopped drift;
one must control their alignment with the common next-event columns.

## 7. Audited boundary

Under (INV\(_\chi\)) with \(\chi<1/2\), proved:

1. macro conflict thinning retains factorial degree and relative
   pair-codegree;
2. the incidence-averaged macro survivor kernel is \(e^{-\Omega(m)}\);
3. logarithmic factorial covariance survives the conflict thinning in
   incidence average;
4. the exact unit-constant degree failure at \(z=m^{-1/2}\); and
5. the corrected constant-factor square-root degree corridor.

Not proved:

1. the mesoscopic survivor-kernel estimate (MSK);
2. hereditary regeneration of the retained logarithmic covariance;
3. the stopped hazard and column estimates (6.4)--(6.5); or
4. the domino-twin near-factor.

The inverse exponent \(\chi<1/2\) is therefore sufficient for the macro
endpoint but not for the full stochastic gate. The next exact failure is
mesoscopic, not macroscopic.
