# Five-slot endpoint-efficient clocks: threshold-face closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves positivity
of the genuine size-five-efficient branch after least-critical endpoint
normalization.  It retains the complete Bellman clock through the
endpoint-period lower bound.  It does not address the size-three- or
size-four-efficient branches, the all-slot Bellman inequality, or an
OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\]

and define the endpoint-period train

\[
 F_A(v)=\sum_{q\ge0}K(qA+v),
 \qquad C(A)=F_A(0).
\tag{0.1}
\]

The proved train estimates include

\[
 C(A)>{1\over25},
 \qquad F_A(v)>{1\over25}\quad(0\le v\le A/4),
 \qquad F_A(v)>0\quad(0\le v\le A/2).
\tag{0.2}
\]

This note adds the two bounds

\[
 \boxed{F_A(v)>-{1\over40}\quad(0\le v\le3A/5),}
\tag{0.3}
\]

and

\[
 \boxed{F_A(v)>-{21\over400}\quad(0\le v\le4A/5).}
\tag{0.4}
\]

They are deliberately coarse; their joint margin is already sufficient
to close the five-slot endpoint branch.

## 1. Exact rational certificates

Let

\[
 P_8(x)=\sum_{j=0}^{8}{x^j\over j!},
 \qquad
 Q_9(x)=\sum_{j=0}^{9}{(-x)^j\over j!}.
\tag{1.1}
\]

For `x>=0`,

\[
 Q_9(x)\le e^{-x}\le{1\over P_8(x)},
\tag{1.2}
\]

with strict inequalities at positive `x`.  We also use

\[
 {157\over50}<\pi<{22\over7}.
\tag{1.3}
\]

The following four checks contain only rational numbers.  Expanding
`P_8,Q_9` and multiplying by their positive denominators gives

\[
\begin{aligned}
 J_L:={}&{1\over5}Q_9\!\left({11\over350}\right)
 -{9\over5P_8(12717/5000)}\\
 &-{14/5+100/157\over P_8(7693/1250)}
 >{1\over25},                                      \tag{1.4}\\
 J_R:={}&{1\over2}Q_9\!\left({11\over56}\right)
 -{3\over2P_8(1413/800)}
 -{5/2+100/157\over P_8(157/32)}
 >{1\over10},                                      \tag{1.5}\\
 B_3:={}&1-{1\over P_8(157/1250)}
 -{1\over P_8(1256/625)}
 -{1\over P_8(26533/5000)}\\
 &-{1+250/1413\over P_8(12717/1250)}
 >-{1\over40},                                     \tag{1.6}\\
 B_4:={}&1-{1\over P_8(157/5000)}
 -{1\over P_8(12717/5000)}
 -{1\over P_8(7693/1250)}\\
 &-{1+500/2983\over P_8(56677/5000)}
 >-{21\over400}.                                   \tag{1.7}
\end{aligned}
\]

No floating-point estimate is used in (1.4)--(1.7).

## 2. Exact train formula

Put

\[
 E(x)=e^{-ax^2}.
\]

For `0<=t<=1`, direct expansion of the compact term followed by all
Gaussian-tail terms gives

\[
 \boxed{
 F_A(At)=1-E(1-t)-\sum_{n\ge0}E(1+t+n).
 }
\tag{2.1}
\]

Let

\[
 h(x)=xe^{-ax^2}.
\tag{2.2}
\]

Differentiation of (2.1) gives

\[
 {d\over dt}F_A(At)
 =2a\left(\sum_{n\ge0}h(1+t+n)-h(1-t)\right).
\tag{2.3}
\]

## 3. Monotonicity on the central-right interval

### Lemma 3.1

The function `t -> F_A(At)` is strictly decreasing on

\[
 {1\over2}\le t\le{4\over5}.
\tag{3.1}
\]

#### Proof

Put

\[
 u=1-t\in[1/5,1/2].
\]

The negative train in (2.3) starts at `2-u>=3/2`, where `h` is decreasing.
The integral test therefore gives

\[
\begin{aligned}
 \sum_{n\ge0}h(2-u+n)
 \le{}&h(2-u)+h(3-u)
       +{e^{-a(3-u)^2}\over2a}.
\end{aligned}
\tag{3.2}
\]

It is enough to prove positivity of

\[
 J(u)=h(u)-h(2-u)-h(3-u)
      -{e^{-a(3-u)^2}\over2a}.
\tag{3.3}
\]

The derivatives of `h` satisfy

\[
 h''(x)=2ax(2ax^2-3)e^{-ax^2}.
\]

Direct differentiation gives

\[
 J''(u)=h''(u)-h''(2-u)-h''(3-u)+h'(3-u).
\tag{3.4}
\]

On `1/5<=u<=1/2`, the four terms on the right side of (3.4) are all
strictly negative: `h''(u)<0`, while `h''(2-u),h''(3-u)>0` and
`h'(3-u)<0`.  Thus `J` is strictly concave.  Its minimum is at an
endpoint.

At those endpoints,

\[
\begin{aligned}
 J(1/5)
 ={}&{1\over5}e^{-\pi/100}
 -{9\over5}e^{-81\pi/100}
 -\left({14\over5}+{2\over\pi}\right)e^{-49\pi/25},\\
 J(1/2)
 ={}&{1\over2}e^{-\pi/16}
 -{3\over2}e^{-9\pi/16}
 -\left({5\over2}+{2\over\pi}\right)e^{-25\pi/16}.
\end{aligned}
\tag{3.5}
\]

The rational certificates (1.4)--(1.5) give

\[
 J(1/5)>{1\over25},
 \qquad J(1/2)>{1\over10}.
\tag{3.6}
\]

Hence `J(u)>0` throughout.  Equations (3.2)--(3.3) show that the
parenthesis in (2.3) is negative, proving the lemma. \(\square\)

## 4. Two coarse endpoint bounds

We use the elementary Gaussian tail estimate

\[
 \sum_{m\ge0}E(z+m)
 \le E(z)+\int_z^\infty E(x)\,dx
 \le E(z)\left(1+{1\over2az}\right)
 \qquad(z>0).
\tag{4.1}
\]

At `t=3/5`, split the first two train terms in (2.1) and apply (4.1) from
`z=18/5` onward:

\[
\begin{aligned}
 F_A(3A/5)\ge{}&1-e^{-\pi/25}-e^{-16\pi/25}
 -e^{-169\pi/100}\\
 &-\left(1+{5\over9\pi}\right)e^{-81\pi/25}.
\end{aligned}
\tag{4.2}
\]

Using (1.2)--(1.3), the right side is bounded below by `B_3` in (1.6).
Thus

\[
 F_A(3A/5)>-{1\over40}.
\tag{4.3}
\]

Similarly, at `t=4/5`, start the residual tail at `z=19/5`:

\[
\begin{aligned}
 F_A(4A/5)\ge{}&1-e^{-\pi/100}-e^{-81\pi/100}
 -e^{-49\pi/25}\\
 &-\left(1+{10\over19\pi}\right)e^{-361\pi/100}.
\end{aligned}
\tag{4.4}
\]

The lower certificate `B_4` in (1.7) gives

\[
 F_A(4A/5)>-{21\over400}.
\tag{4.5}
\]

The known positivity of `F_A` on `[0,A/2]`, together with Lemma 3.1 and
(4.3)--(4.5), proves the uniform bounds (0.3)--(0.4).

## 5. Endpoint-period closure of the five-slot branch

### Theorem 5.1

Let

\[
 (c_0,c_1,c_2,c_3,c_4,c_5)
\]

be a saturated first-crossing table assigned to `h=5` by the least
maximizer rule.  Then its Bellman functional is strictly positive.

#### Proof

The least-critical endpoint theorem gives

\[
 c_5=A.
\tag{5.1}
\]

Endpoint maximal efficiency gives

\[
 0\le c_i\le{iA\over5}
 \qquad(1\le i\le4).
\tag{5.2}
\]

The endpoint-period lower bound applies directly to the actual Bellman
clock:

\[
 \Phi(c)\ge C(A)+F_A(c_1)+F_A(c_2)+F_A(c_3)+F_A(c_4).
\tag{5.3}
\]

No eventual Apéry witness or finite head is discarded in (5.3): for
capacity `5q+r`, the literal configuration of `q` endpoint generators and
the size-`r` generator supplies the comparison value `qA+c_r`; at `q=0`
internal superadditivity gives equality.

Now (0.2)--(0.4) and (5.2) give

\[
\begin{aligned}
 \Phi(c)
 &>{1\over25}+{1\over25}+0-{1\over40}-{21\over400}\\
 &= {1\over400}>0.
\end{aligned}
\tag{5.4}
\]

This proves the theorem. \(\square\)

### Corollary 5.2

After first-crossing deletion, endpoint saturation, and assignment by the
least maximizer, a nonpositive five-slot table cannot lie in the
size-five-efficient branch.  Together with the separately proved
size-two-efficient closure, any remaining five-slot obstruction must be
assigned to size three or size four.

## 6. Scope

The proof does not replace the sixteen endpoint-efficient Apéry paths by
an eventual approximation.  It bypasses their availability issue using a
literal endpoint-period lower bound on the full Bellman clock.  The
remaining five-slot work is confined to the size-three- and
size-four-efficient branches.
