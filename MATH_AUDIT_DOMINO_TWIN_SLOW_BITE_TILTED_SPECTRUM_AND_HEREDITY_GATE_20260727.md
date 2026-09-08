# Domino twins: stopped slow-bite degrees, the tilted overlap spectrum, and the heredity gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad R=m-q_0,\qquad q_0=a\sqrt m+O(1),
 \qquad K=2n=4m,
\tag{0.1}
\]

and work on the parity subsequence on which \(R\) is odd. The slow bite
must use the **simple** domino-necklace catalogue. Its degree is

\[
 \boxed{D=2^{1-m}R!(n-R)!,}
\tag{0.2}
\]

not the labelled-presentation degree \(2nR!(n-R)!\). The conclusions of
this audit are the following.

1. The static factorial-overlap theorem descends unchanged to the simple
   quotient. Parallel labelled presentations are harmless in that static
   average, but they are not independent choices and cannot be used in a
   slow bite.

2. The claimed family of \(\Theta(n)\) distinct edges sharing \(K-4\)
   targets is a labelled-presentation artefact. Swapping entries inside
   one domino fixes the simple superpacket exactly.

3. A time-zero bound cannot simply be reused unchanged under thinning.
   If a fixed edge \(F\ni X\) is forced to remain live and other targets
   survive independently with density \(z\), the exact reference degree
   and factorial numerator are

   \[
    \bar d_F(z)=z^{K-1}\sum_{j=0}^{K-2}a_j(F,X)z^{-j},
   \tag{0.3}
   \]

   \[
    S_{p,F}(z)=z^{K-1}\sum_{j=0}^{K-2}(j)_p
                              a_j(F,X)z^{-j},
   \tag{0.4}
   \]

   where \(a_j(F,X)\) counts simple edges \(G\ni X\), \(G\ne F\), with
   \(|F\cap G|-1=j\). Thus the correct comparison is the exponentially
   tilted ratio

   \[
    b_{p,F}(z)=\frac{S_{p,F}(z)}{\bar d_F(z)}.
   \tag{0.5}
   \]

   Here \(\bar d_F\) is the competitor degree, excluding the protected
   row \(F\); the full conditional link degree is \(1+\bar d_F\).
   The correct comparison is not the time-zero value \(b_{p,F}(1)\).
   Moreover \(b_{p,F}(z)\) is
   nondecreasing as \(z\) decreases.

4. For the actual stopped slow bite, let \(N_{j,t}(X,F)\) be the number
   of current link rows in overlap stratum \(j\). The exact compensated
   variables are

   \[
    \boxed{
    Y_{j,t}=N_{j,t}z_t^{-(K-1-j)}.}
   \tag{0.6}
   \]

   Their generator contains the hazard discrepancy

   \[
    h_{j,t}-(K-1-j)h_t,
   \tag{0.7}
   \]

   where \(h_{j,t}\) is the actual conditional death hazard of a row in
   stratum \(j\) and \(h_t=-\dot z_t/z_t\). There is no restoring term in
   (0.7). Hence no scalar self-correction follows automatically; a
   restoring sign would itself be a theorem about the full overlap
   spectrum.

5. The nominal degree can be tracked arithmetically through
   \(O(m\log m)\) rounds, but this does not prove its probabilistic
   regeneration. At \(z=m^{-1/3}\),

   \[
    \log(Dz^{K-1})=\frac23m\log m-O(m),
   \tag{0.8}
   \]

   so the reference link is still factorially large. At
   \(z=c/\sqrt m\),

   \[
    \log(Dz^{K-1})
      =(4\log c-2-\log2)m+O(\log m).
   \tag{0.9}
   \]

   Thus a square-root stop has exponentially many reference choices only
   for

   \[
    c>c_*:=\exp((2+\log2)/4).
   \tag{0.10}
   \]

6. Logarithmic static factorial moments do not control (0.3)--(0.5): the
   factor \(z^{-j}\) reads overlap strata far above logarithmic order.
   The exact remaining theorem is an all-scale, incidence-weighted bound
   on the integrated discrepancies (0.7), together with their common-
   next-edge column moments. That theorem is not proved by the two source
   notes.

Therefore the requested stopped/hereditary factorial theorem is **not
proved**. More sharply, its time-zero normalization is not the natural
dynamic invariant. The strongest exact result is the tilted-spectrum
reduction below. It removes the spurious labelled near-parallel obstruction and
isolates the genuine dynamic condition without invoking classical
Pippenger--Spencer.

## 1. Passing the static theorem to the simple quotient

Let \(\mathcal Q_{\rm lab}\) be the anchored labelled presentation and
\(\mathcal Q\) the simple catalogue of distinct supports. Every simple
edge has exactly

\[
                         \mu=n2^m
\tag{1.1}
\]

anchored presentations. Consequently

\[
 D_{\rm lab}=\mu D.
\tag{1.2}
\]

Fix simple edges \(F,G\) and put

\[
                         w_p(F,G)=(|F\cap G|-1)_p.
\tag{1.3}
\]

The weight depends only on the supports. Hence

\[
 {1\over D_{\rm lab}}
 \sum_{G_{\rm lab}\ni X}w_p(F,G_{\rm lab})
 ={1\over D}\sum_{G\ni X}w_p(F,G).
\tag{1.4}
\]

If the labelled convention retains presentations parallel to \(F\),
their normalized contribution is \(\mu(K-1)_p/D_{\rm lab}\), namely
\((K-1)_p/D\), and is factorially negligible for
\(p=O(\log m)\). Removing the self-edge gives the simple static bound

\[
 \boxed{
 {1\over D}\sum_{\substack{G\ni X\\G\ne F}}w_p(F,G)
 \le(Cp)^{Cp}m^{-2}
 \qquad(1\le p\le C_0\log m).}
\tag{1.5}
\]

Thus the static theorem survives quotienting. The dynamic interpretation
does not: the \(\mu\) presentations of one support cannot be marked as
separate matching options.

### Lemma 1.1 (the labelled \(K-4\) family collapses)

Let \(P=(x_0,\ldots,x_{n-1})\), and let \(s_i\) exchange
\(x_{2i},x_{2i+1}\). Then

\[
                         Q(P\circ s_i)=Q(P).
\tag{1.6}
\]

#### Proof

The simple support \(Q(P)\) is determined by the unoriented cyclic
necklace of the unordered dominoes

\[
 B_i=\{x_{2i},x_{2i+1}\}.
\]

The operation \(s_i\) changes only the orientation chosen inside the
same unordered domino. It fixes the necklace and therefore fixes every
four-boundary extension in the domino normal form. Hence it fixes
\(Q(P)\). \(\square\)

This corrects the macroscopic-overlap diagnosis based on these
\(s_i\)'s. Distinct simple edges can still share an entire \(n\)-target
ordinary component packet, but internal domino flips do not create
distinct columns.

## 2. Exact conditional degree under an ideal survivor tilt

Fix a simple edge \(F\ni X\). For \(0\le j\le K-2\), define

\[
 a_j=a_j(F,X)
 =|\{G\in\mathcal Q:G\ni X,\ G\ne F,
                         \ |F\cap G|-1=j\}|.
\tag{2.1}
\]

Force every target of \(F\) to survive, and retain every target outside
\(F\) independently with probability \(z\). A row \(G\) in stratum
\(j\) has

\[
 |G\setminus F|=K-|F\cap G|=K-1-j
\tag{2.2}
\]

targets whose survival is not already forced. Therefore its survival
probability is exactly \(z^{K-1-j}\). Linearity of expectation proves
(0.3)--(0.4).

This calculation uses one common survivor set for every stratum. It is
not an independent-rank heuristic.

### Theorem 2.1 (monotone survivor tilt)

For every \(p\ge1\), the reference ratio \(b_{p,F}(z)\) in (0.5) is
nondecreasing as \(z\) decreases.

#### Proof

Put \(\theta=-\log z\) and give \(j\) weight

\[
                         a_je^{\theta j}.
\]

After cancelling the common factor \(z^{K-1}\), equation (0.5) is the
expectation of \((j)_p\) under the normalized tilted weights. Hence

\[
 {d\over d\theta}b_{p,F}(e^{-\theta})
 =\operatorname {Cov}_\theta((j)_p,j)\ge0.
\tag{2.3}
\]

The covariance is nonnegative because both functions are nondecreasing;
equivalently, its doubled numerator is

\[
 {1\over2}\sum_{i,j}\pi_i\pi_j
 ((i)_p-(j)_p)(i-j)\ge0.
\]

This proves the assertion. \(\square\)

Thus even perfect product-style regeneration does not preserve the
time-zero ratio. Any stopped theorem with a fixed right side ignores a
real survivor bias toward rows overlapping the protected live edge.

## 3. The exact stopped overlap-spectrum generator

Consider a continuous slow matching process. At time \(t\), let
\(L_t(X)\) be the live link of \(X\), and stop every monitor when \(X\)
or \(F\) dies. While the monitor is live, put

\[
 N_{j,t}=|\{G\in L_t(X):G\ne F,\ |F\cap G|-1=j\}|.
\tag{3.1}
\]

For a possible next selected edge \(e\), disjoint from \(F\), put

\[
 B_{j,t}(e)=
 |\{G\text{ counted by }N_{j,t}:G\cap e\ne\varnothing\}|.
\tag{3.2}
\]

If \(e\) has predictable clock rate \(\nu_t(e)\), then the stopped
generator is exactly

\[
 \boxed{
 \mathcal G_tN_{j,t}
 =-\sum_{e\cap F=\varnothing}\nu_t(e)B_{j,t}(e).}
\tag{3.3}
\]

When \(N_{j,t}>0\), define its actual average death hazard by

\[
 h_{j,t}={1\over N_{j,t}}
 \sum_{e\cap F=\varnothing}\nu_t(e)B_{j,t}(e).
\tag{3.4}
\]

Let \(z_t\) be a positive deterministic reference density and put

\[
                         h_t=-{\dot z_t\over z_t}.
\tag{3.5}
\]

### Theorem 3.1 (exact compensated spectrum)

For \(Y_{j,t}=N_{j,t}z_t^{-(K-1-j)}\),

\[
 \boxed{
 {\mathcal G_tY_{j,t}\over Y_{j,t}}
 =(K-1-j)h_t-h_{j,t}.}
\tag{3.6}
\]

Here the left side includes the deterministic time derivative of the
factor \(z_t^{-(K-1-j)}\).

#### Proof

Equation (3.3) says
\(\mathcal G_tN_{j,t}=-h_{j,t}N_{j,t}\). Differentiating the
deterministic multiplier gives

\[
 {d\over dt}z_t^{-(K-1-j)}
 =(K-1-j)h_tz_t^{-(K-1-j)}.
\]

The product rule proves (3.6). \(\square\)

Let \(\mathcal M_{j,t}\) be the martingale part of \(Y_{j,t}\). Since
one selected edge changes \(Y_{j,t}\) by
\(-z_t^{-(K-1-j)}B_{j,t}(e)\), its predictable quadratic variation is
exactly

\[
 {d\langle\mathcal M_j\rangle_t\over dt}
 =z_t^{-2(K-1-j)}
   \sum_{e\cap F=\varnothing}\nu_t(e)B_{j,t}(e)^2.
\tag{3.6a}
\]

For every integer \(\ell\ge2\), the corresponding absolute jump-moment
rate is

\[
 z_t^{-\ell(K-1-j)}
 \sum_{e\cap F=\varnothing}\nu_t(e)B_{j,t}(e)^\ell.
\tag{3.6b}
\]

Thus the least stopped concentration input, after division by
\(Y_{j,t}^\ell\), is the relative column hierarchy

\[
 \int_0^T {1\over N_{j,t}^{\ell}}
 \sum_{e\cap F=\varnothing}\nu_t(e)B_{j,t}(e)^\ell\,dt=o(1)
 \qquad(\ell=2,L),
\tag{3.6c}
\]

with the usual truncation for small \(N_{j,t}\). These are common-next-
edge column moments in the current residual, not the time-zero row
factorial moments.

The integrated deterministic condition corresponding to (3.6) is

\[
 \boxed{
 \sup_{j:\,N_{j,0}>0}
 \left|\int_0^T
       (h_{j,t}-(K-1-j)h_t)\,dt\right|=o(1).}
\tag{3.7}
\]

For strata whose reference mass tends to infinity, together with the
appropriate stopped column quadratic and large-jump moments, (3.7) would
regenerate the stratum; smaller strata require incidence-weighted
quarantine. But (3.6) has no explicit term of the form

\[
                  -c\,(Y_{j,t}/Y_{j,0}-1).
\]

Thus the natural compensated spectrum has no automatic self-correction.
Any restoring force would have to be proved as a sign estimate for the
hazard discrepancy in (3.6). The static factorial theorem determines
\(Y_{j,0}\) only after summing over \(j\); it gives neither (3.7) nor
such a sign.

## 4. Recovering the individual factorial generator

Put

\[
 \bar d_t(X)=d_t(X)-1=\sum_jN_{j,t},
 \qquad
 S_{p,t}(X,F)=\sum_j(j)_pN_{j,t},
 \qquad
 A_{p,t}={S_{p,t}\over \bar d_t(X)}.
\tag{4.1}
\]

The omitted row is the protected row \(F\), which never dies before the
monitor is stopped. For an event \(e\) disjoint from \(F\), put

\[
 B_X(e)=\sum_jB_{j,t}(e),
 \qquad
 C_{p,X,F}(e)=\sum_j(j)_pB_{j,t}(e).
\tag{4.2}
\]

Direct subtraction gives

\[
 \boxed{
 \Delta_eA_{p,t}
 ={A_{p,t}B_X(e)-C_{p,X,F}(e)
   \over \bar d_t(X)-B_X(e)}.}
\tag{4.3}
\]

Thus the drift is positive precisely when \(e\) deletes below-average
factorial weight from the current link. It has no deterministic sign.

For a density-dependent comparison \(b_{p,F}(z_t)\), the unnormalized
error

\[
 M_{p,t}=S_{p,t}-b_{p,F}(z_t)\bar d_t(X)
\tag{4.4}
\]

has event jump

\[
 \Delta_eM_{p,t}=b_{p,F}(z_t)B_X(e)-C_{p,X,F}(e)
\tag{4.5}
\]

and deterministic transport

\[
 -{d\over dt}b_{p,F}(z_t)\,\bar d_t(X).
\tag{4.6}
\]

Equations (4.5)--(4.6) exhibit the only possible cancellation: the
survivor-tilt increase in Theorem 2.1 must be matched by the actual
factorial-weighted deletion covariance. The time-zero diameter sum does
not provide that equality after conditioning.

## 5. Conditional degree arithmetic over \(O(m\log m)\) rounds

The simple degree (0.2) satisfies, by Stirling's formula,

\[
 \log D
 =2m\log m-(2+\log2)m+O_a(\log m).
\tag{5.1}
\]

In a slow bite whose nominal density satisfies

\[
                         z_t=e^{-t/K},
\tag{5.2}
\]

reaching \(z\) takes \(t=K\log(1/z)\). Hence both
\(z=m^{-1/3}\) and \(z=c/\sqrt m\) require \(O(m\log m)\) rescaled
rounds. Substitution in

\[
                         D_z=Dz^{K-1}
\tag{5.3}
\]

gives (0.8)--(0.10).

This is the complete conditional-degree arithmetic. It shows that
\(m^{-1/3}\) is safely above entropy exhaustion and already yields the
\(o(W)\) scalar annular floor required by the paired-counterexample
route. It does **not** show that the random residual degree equals
\(D_z\). Such a conclusion is exactly the \(j\)-summed consequence of
(3.7) plus its martingale column estimates.

## 6. Why logarithmic factorial control does not close the spectrum

Let \(L=C_0\log m\). From the static theorem and
\((j)_L\mathbf1_{\{j\ge L\}}\le (j)_L\), one obtains only

\[
 {a_j\over D}
 \le{(CL)^{CL}m^{-2}\over(j)_L}
 \qquad(j\ge L).
\tag{6.1}
\]

After conditioning on \(F\) being live, stratum \(j\) is amplified
relative to a generic row by \(z^{-j}\). Thus (6.1) yields

\[
 {a_jz^{-j}\over D}
 \le { (CL)^{CL}m^{-2}z^{-j}\over(j)_L}.
\tag{6.2}
\]

At \(z=m^{-1/3}\), take for example \(j=\lfloor m^{1/2}\rfloor\).
The logarithm of the numerator contributed by \(z^{-j}\) is

\[
                         \frac j3\log m,
\]

whereas \(\log (j)_L=O((\log m)^2)\). The right side of (6.2) is
therefore enormous. This does not prove that the actual stratum is large;
it proves rigorously that logarithmic factorial moments do not bound its
survivor tilt.

The logical separation can be made literal. Put \(j_0=\lfloor\sqrt
m\rfloor\), and define

\[
 \varepsilon_m
 =m^{-2}\min_{1\le p\le L}
       { (Cp)^{Cp}\over(j_0)_p}.
\tag{6.2a}
\]

An abstract overlap law having mass \(\varepsilon_m\) at \(j_0\) and
the remaining mass at \(0\) satisfies every static inequality through
order \(L\). Since \(\log j_0=(1/2+o(1))\log m\),

\[
 \log\varepsilon_m
 =-O((\log m)^2),
\tag{6.2b}
\]

whereas at \(z=m^{-1/3}\),

\[
 \log(\varepsilon_m z^{-j_0})
 ={1\over3}\sqrt m\log m-O((\log m)^2)\longrightarrow+\infty.
\tag{6.2c}
\]

Thus no theorem about the tilted spectrum follows formally from all the
proved logarithmic factorial inequalities. Catalogue geometry beyond
those inequalities is indispensable.

The all-scale issue survives removal of the false labelled \(K-4\)
family. The simple catalogue has genuine distinct columns sharing an
entire \(n\)-target component packet. There are at most \(2^m\) such
neighbours of a fixed edge, because that edge has \(2^m\) component
traces and every trace belongs to exactly two simple superpackets. Their
own contribution at \(z=m^{-1/3}\) is at most

\[
 {2^m\over D}z^{-(K-2)}
 =\exp[-(2/3+o(1))m\log m],
\tag{6.3}
\]

where we used only \(|F\cap G|-1\le K-2\) for distinct supports. Thus
the known whole-component class is harmless at this safer stopping
density. What remains unclassified is the complete intermediate overlap
spectrum between logarithmic and linear order.

## 7. Exact proved/open boundary

Proved here:

1. the labelled static factorial theorem descends to the simple quotient;
2. internal domino flips give the same simple edge, eliminating the
   purported distinct \(K-4\) family;
3. the exact conditional product reference (0.3)--(0.5);
4. monotonicity of the survivor-tilted factorial ratio;
5. the exact stopped stratum generator (3.3)--(3.7);
6. the exact individual normalized generator (4.3)--(4.6);
7. the full simple-degree arithmetic through \(O(m\log m)\) nominal
   rounds; and
8. the failure of logarithmic factorial moments to control intermediate
   survivor tilts.

Not proved:

1. the integrated stratum-hazard estimate (3.7) along the actual slow
   bite;
2. the associated common-next-edge quadratic and large-jump bounds;
3. a stopped all-scale overlap-spectrum corridor; or
4. the domino-twin near-factor.

The sought scalar self-correcting invariant does not emerge from the
proved inputs: the exact compensated generator leaves its drift equal to
the conditional hazard covariance itself. A successful slow-bite proof
must therefore do one of
two genuinely new things:

* prove (3.7) incidence-weightedly for the full overlap spectrum, with an
  all-scale quarantine of exceptional strata; or
* replace residual regeneration by a one-shot matching/absorption
  argument.

Classical Pippenger--Spencer is neither used nor available.
