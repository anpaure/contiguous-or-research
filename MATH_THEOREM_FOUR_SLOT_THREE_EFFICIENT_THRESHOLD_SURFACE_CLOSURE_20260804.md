# Four-slot three-efficient clocks: closure of the threshold surface

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It closes the
`P+u=A` boundary surface left by the exact three-efficient period reduction.
It does not close the second surface `P+u=2y`, the `w=2u` pulse system, or
all four-slot tables.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_A(v)=\sum_{q\ge0}K(qA+v),
 \qquad C(A)=F_A(0).
\tag{0.1}
\]

The threshold surface consists of internally superadditive tables

\[
                    (0,x,y,P,A),
 \qquad P=A-u,
\tag{0.2}
\]

with

\[
 0\le x\le u\le {A\over4},
 \qquad 2u\le y\le {A\over2}.
\tag{0.3}
\]

## 1. A small-shift upper bound

### Lemma 1.1

For `0<=v<=A/4`,

\[
                         \boxed{F_A(v)<{1593\over22000}.}
\tag{1.1}
\]

### Proof

Write `v=At`, `0<=t<=1/4`, and put `a=A^2=pi/4` and
`E(s)=exp(-as^2)`.  Direct expansion gives

\[
 F_A(At)
 =1-E(1-t)-\sum_{n\ge0}E(1+t+n).
\tag{1.2}
\]

The pair `E(1-t)+E(1+t)` is nondecreasing in `t`.  Indeed its logarithmic
derivative has the sign of

\[
                   \tanh(2at)-t.
\]

Since `2a=pi/2>3/2`, it is enough to note that
`tanh(3t/2)>=t` on `[0,1/4]`.  The function
`tanh(3t/2)-t` is concave, vanishes at zero, and at `t=1/4` is larger than

\[
 {3/8\over1+3/8}-{1\over4}
 ={3\over11}-{1\over4}>0;
\]

here `tanh x>x/(1+x)` follows from `e^(2x)>1+2x`.
Consequently

\[
                  E(1-t)+E(1+t)\ge2e^{-\pi/4}.       \tag{1.3}
\]

We use two exact rational bounds.  First,

\[
                         e^{-\pi/4}>{5\over11}.       \tag{1.4}
\]

To see this, use `pi/4<11/14=1/2+2/7`.  The exponential series gives

\[
 e^{1/2}<{33\over20},
 \qquad e^{2/7}<{4\over3};
\]

for the first inequality, sum through degree three and bound the remaining
tail geometrically, while for the second sum through degree two and use
successive ratio at most `1/14`.  Thus

\[
 e^{\pi/4}<e^{11/14}<{33\over20}{4\over3}={11\over5}.
\]

Second, the audited quarter-shift Gaussian estimate gives

\[
                         E(9/4)=e^{-81\pi/64}>{37\over2000}.    \tag{1.5}
\]

Since `2+t<=9/4`, equations (1.2)--(1.5) imply

\[
\begin{aligned}
 F_A(At)
 &<1-{10\over11}-{37\over2000}\\
 &={1593\over22000}.
\end{aligned}
\]

This proves (1.1). \(\square\)

## 2. Reflection and the endpoint-period lower bound

The exact reflected-train identity is

\[
 F_A(v)+F_A(A-v)
 =-4\sum_{m\ge1}e^{-4\pi m^2}
                  \cos(2\pi m v/A).
\tag{2.1}
\]

The standard theta-tail estimate therefore gives

\[
                         F_A(A-v)>-F_A(v)-{1\over20000}.
\tag{2.2}
\]

We also use the already proved train bounds

\[
 C(A)>{1\over25},
 \qquad F_A(v)>{1\over25}\quad(0\le v\le A/4),
 \qquad F_A(v)>0\quad(0\le v\le A/2).
\tag{2.3}
\]

### Lemma 2.1 (endpoint-period lower bound)

Let `(c_0,...,c_n)` be internally superadditive, with `c_n=A`, and let
`V` be its Bellman clock.  Then

\[
             \sum_{m\ge0}K(V_m)
             \ge\sum_{r=0}^{n-1}F_A(c_r).           \tag{2.4}
\]

### Proof

For `m=qn+r`, `0<=r<n`, the configuration with `q` endpoint generators
and one generator of size `r` gives

\[
                         V_{qn+r}\ge qA+c_r.
\]

At `q=0`, internal superadditivity gives equality `V_r=c_r`.  At `q>=1`,
both sides lie in `[A,infinity)`, where `K` is increasing.  Sum the
termwise inequalities over all residues. \(\square\)

## 3. Positivity of the threshold surface

### Theorem 3.1

Every table (0.2)--(0.3) has strictly positive Bellman functional.  In
fact,

\[
                 \boxed{\sum_{m\ge0}K(V_m)>{1659\over220000}.}
\tag{3.1}
\]

### Proof

Apply Lemma 2.1 with `n=4`, then use `P=A-u`:

\[
 \sum_mK(V_m)
 \ge C(A)+F_A(x)+F_A(y)+F_A(A-u).
\tag{3.2}
\]

Equations (2.2)--(2.3), Lemma 1.1, and (0.3) give

\[
\begin{aligned}
 \sum_mK(V_m)
 &>{1\over25}+{1\over25}+0
   -{1593\over22000}-{1\over20000}\\
 &={1659\over220000}>0.
\end{aligned}
\]

This proves (3.1). \(\square\)

### Corollary 3.2

On the `w=y` face of the three-slot-efficient four-slot regime, the
period-monotonicity reduction no longer leaves the surface `P+u=A`.
Only the surface `P+u=2y`, the separately stated normalized large-residue
face, and the `w=2u` pulse system remain.

## 4. Scope

The proof uses a genuine Bellman lower bound rather than dropping the
finite transient in the three-efficient normal form.  It therefore closes
the complete threshold surface (0.2)--(0.3), but makes no claim on the
other three-efficient surfaces, all `n=4`, the universal Bellman inequality,
or `nu(k)<=B(k)+O(1)`.
