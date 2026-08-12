# Independent audit: Rayleigh first-transform exact two-to-three count window

**Date:** 2026-08-05  
**Method:** independent pure-mathematical reconstruction; no search or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`  
**Audited source SHA-256:**
`1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`  
**Verdict:** **GO with one scope clarification.**  The strict inequalities
`2J_2<S_2<3J_2` follow from the displayed rational enclosures.  They prove
only the scalar occurrence-count window.  Since the residual job support is
unbounded while every residual socket is below `b`, they do not by themselves
permit a literal policy using only two or three sockets per job.

## 1. Mass identities

After the first equal-level subtraction, the transformed job density is
`u'` on `(0,infinity)` and the transformed socket density is `-K'` on
`(0,b)`.  Cancelling their common density `u'` on `(0,b)` leaves

\[
 J_2=\int_b^\infty u'(t)\,dt=-u_b
\]

and

\[
 S_2=\int_0^b(-K'(t)-u'(t))\,dt
     =K_0-K(b)-\bigl(u_b-u(0)\bigr)
     =K_0+m-u_b.
\]

Here `K(b)=0` and `u(0)=m`.  Thus (1.1) has the correct signs and no endpoint
atom is missing.

## 2. Coarse exact brackets

The bracket

\[
 {4431\over5000}<A={\sqrt\pi\over2}<{8863\over10000}
\]

follows from `333/106<pi<355/113` after squaring the positive rational
endpoints.  The exponential-tail estimate (2.1) then converts every entry of
the table (2.3) into a finite rational comparison.  The logical uses of that
table are correct:

* the signs of `K'` at `0.772` and `0.788` trap the unique minimum `c`;
* `e^{-(A-c)^2}<0.991` and `e^{-(A+c)^2}<0.064` give `m>-0.055`;
* `m<=K(0.78)<-0.05` gives the opposite strict bound;
* together with `0.088<K_0<0.09`, these yield
  `0.033<K_0+m<0.04`.

The inequalities are deliberately loose, but their directions are all the
ones needed later.

## 3. Separation level

The signs `K(0.46)>0>K(0.48)` imply `0.46<b<0.48`.  Let
`e=ell(u_b)` and `R=r(u_b)=e+b`.

At left endpoint `0.55`, the displayed comparison

\[
 K(0.55)>K(1.03)>K(0.55+b)
\]

uses `0.55+b<1.03` and monotonicity of the right inverse branch.  Therefore
the equal-level right endpoint lies beyond `0.55+b`, so its separation is
larger than `b`.  Since separation decreases as the left endpoint moves from
`b` toward `c`, this gives `e>0.55`.

Likewise, at left endpoint `0.60`,

\[
 K(0.60)<K(1.06)<K(0.60+b)
\]

shows that the equal-level right endpoint lies before `0.60+b`; hence
`e<0.60`.  Consequently

\[
 1.01<R<1.08,
 \qquad 1.8962<A+R<1.9663.
\]

Since `R>A`, the right branch is `K(R)=-e^{-(A+R)^2}`.  Monotonicity of the
exponential and the certified endpoint comparisons give

\[
 0.02<-u_b<0.03.
\]

## 4. The strict count window

Put `P=K_0+m` and `q=-u_b`.  The independent brackets are

\[
 0.033<P<0.04,
 \qquad 0.02<q<0.03.
\]

Hence

\[
 P-q>0.033-0.03>0,
 \qquad
 P-2q<0.04-2(0.02)=0.
\]

As `S_2=P+q` and `J_2=q`, these are exactly

\[
 S_2-2J_2=P-q>0,
 \qquad
 3J_2-S_2=2q-P>0.
\]

Thus `2J_2<S_2<3J_2` is exact.

## 5. Scope clarification

The count identity fixes the scalar masses of a hypothetical two/three
mixture:

\[
 \alpha=S_2-2J_2,
 \qquad
 \beta=3J_2-S_2,
\]

where `alpha` is the mass of three-socket jobs and `beta` the mass of
two-socket jobs.  It does **not** imply that such a configuration coupling
exists.  Indeed, before a separate tail removal the job support is
unbounded, whereas all sockets lie in `(0,b)`; every job larger than `3b`
requires at least four positive sockets.  The theorem's final sentence must
therefore be read exactly as stated there: no arity outside `{2,3}` is forced
by the *aggregate count row*, not by literal support geometry.

This does not weaken the numerical theorem.  It identifies the next valid
step: first remove every high-arity tail by an exact kernel, then recheck the
strict two/three count window and the support bound on the compact remainder
before attempting a two/three packet coupling.
