# First variation of asymmetric short-axis rank bounds

2026-09-08. Pure analytic calculation; no computation. Root and independent
direct-route full audits passed. These are rank-antichain LOWER bounds, not chain
partition upper bounds. A constructive partition attaining their first
variation has not been proved.

## 1. Poset and exact polynomial

In one four-axis staircase, let the short coordinate occur at position
p in {1,2,3,4}. Its low and high lengths are u,v, with u+v=r<=2s.
Each other coordinate has length 2s and half-cut s. Absorb a fifth
coordinate chain of length 2s into this staircase. Call the resulting
ordered product Q_p(u,v;s). Every coordinate is an actual chain index.

The threshold boxes give the exact rank polynomial

    [s]^3[2s] ( [u] sum_(j=0)^(p-1) q^(js)
                    + q^u[v] sum_(j=p)^4 q^((j-1)s) )
      =[s]^2[2s] ( [u][ps]
                +q^(u+(p-1)s)[v][(5-p)s] ).        (1)

Here [b]=1+q+...+q^(b-1), and [0]=0. The unabsorbed staircase
membership is s^3 M_p, where

    M_p=p u+(5-p)v.                                (2)

Paired with the other standard four-axis staircase, of membership
5s^4 and chain count s^3, a partition of Q_p into W_p chains would
give principal charge

    2s^7 M_p + 5s^4 W_p.                           (3)

Equation (3) is a legal upper ledger ONLY when an actual covering chain
family with the displayed membership and chain count has been supplied.
Replacing W_p by a rank size does not supply such a family.

## 2. Continuum central-rank formula

Take s to infinity with

    r=2ts+O(1), u=(t+delta)s+O(1),
    v=(t-delta)s+O(1), 0<t<=1, |delta|<=t.

The ambient index-sum range is 0,...,r+8s-5, with scaled center 4+t.
Both extremes occur when u,v>0; the density formula extends continuously
to an empty low or high part even though some extremes then disappear.
Let f_C be the unnormalized convolution density of intervals
[0,1],[0,1],[0,2]. Its total mass is two and it is symmetric about two.
Its twice integrated density is

    H(x)=[x_+^4-2(x-1)_+^4+2(x-3)_+^4-(x-4)_+^4]/24,
    J(x)=H(x)+H(5-x).                              (4)

Convolving (1), the scaled coefficient at a nearest central rank tends
to the following value (the rank size is s^4 times it, plus o(s^4)):

    Q_p(t,delta)
       = J(p+delta)-H(p-t)-H(5-p-t)-H(|delta|).     (5)

Derivation: for the low box, reflect f_C around two, and for the high
box reverse both integration variables. The two contributions become

    F_(t+delta,p)(t)+F_(t-delta,5-p)(t),
    F_(w,L)(t)=integral_0^w integral_0^L
                                  f_C(x+y-t)dy dx.

Since H''=f_C,

    F_(w,L)(t)=H(w+L-t)-H(L-t)-H(w-t)+H(-t).

Here H(-t)=0, and H(delta)+H(-delta)=H(|delta|). This proves (5).
The density itself follows by expanding (1-q)^2(1-q^2), whose
coefficients are 1,-2,0,2,-1; no probability law for chain partitions
or physical roots is used.

## 3. At equal total lengths, the largest rank has this first variation

At t=1 and delta=0, (1) simplifies to [s]^3[2s][5s]. Its limiting rank
density has a unique maximum two at scaled rank five. Near that point
it is exactly

    f_0(5+h)=2-|h|^4/24,       |h|<=1.             (6)

Indeed the convolution of [0,1]^3 and [0,2] has total mass two, support
[0,5], and density x^3/6 for 0<=x<=1; convolution with [0,5] removes
the corresponding endpoint tail of mass |h|^4/24. Positivity of the
inner density in (0,5) also proves uniqueness of the maximum.

The perturbed limiting density is a finite sum of truncated fourth
powers. It and its delta derivative are uniformly continuous on a
common compact support. Therefore every maximizing rank tends to five
as delta tends to zero, and its maximum has the same first derivative
as the coefficient at five. More quantitatively, the delta derivative
is uniformly Lipschitz in the rank variable near five, while (6) loses
a fixed multiple of h^4. Optimizing -h^4/24+O(|delta h|) and retaining
the uniform O(delta^2) Taylor remainder gives an O(|delta|^(4/3)) error.

Differentiating (5) thus proves for the largest limiting rank density

    max_rank f_p(rank,delta)
       =2+d_p delta+O(|delta|^(4/3)),
    (d_1,d_2,d_3,d_4)=(-11,-5,5,11)/6.             (7)

For clarity, H'(1)=1/6,H'(2)=1,H'(3)=11/6,H'(4)=2, while H'(|delta|)
vanishes at zero. Hence d_p=H'(p)-H'(5-p), as displayed.
This statement first takes the large-s rank-density limit, and then
delta to zero; it does not assert a uniform estimate at every mesh scale.

## 4. Literal template imbalance and the unproved constructive gate

For any coordinate of the exact fourteen-row eight-bit template, let
n_p count its occurrences at shore position p. Exactness of the middle
rank gives

    sum_p n_p=14,           sum_p p n_p=35.         (8)

Indeed the coordinate occurs in 5-p rank-four row targets, whose total
must be binom(7,3)=35. Thus the summed membership term in (3) is
independent of delta. However (8) does not force reversal-symmetric
position counts.

For coordinate zero of the literal Appendix A.7 template, its successive
positions in the fourteen displayed rows are

    1,1,1,1,3,3,3,4,3,4,3,3,2,3.

Consequently (n_1,n_2,n_3,n_4)=(4,1,7,2), and

    sum_p n_p d_p=4/3.                             (9)

A negative delta lowers the SUM of the largest rank lower bounds to
first order at t=1. If actual chain partitions of all the absorbed
posets attained the first variations in (7), (3) would have summed
charge

    280s^8+(20/3)delta s^8+o(|delta|s^8),           (10)

in the iterated large-s, small-delta sense. Dividing by actual volume
(2s)^9 and multiplying by the principal length a=2s would change
alpha=35/32 by (5/192)delta to first order.

The premise of (10) is OPEN. In particular, these asymmetric posets
have not been proved Sperner or supplied with a chain partition of
their largest-rank size. Non-rank antichains could force a larger width,
and separate generalized-hook remnants may create a first-order cost.
Removing duplicate chain images also requires literal coverage and
membership accounting. The rank calculation therefore identifies a
possible constructive direction and invalidates a naive extension of
the symmetric rank barrier; it does not improve a terminal upper bound
or the unconditional record.

## 5. An explicit displaced cut survives maximizing over ranks

The following is a rigorous continuum RANK statement at t=1. Put

    epsilon=2^(-15),              delta=-epsilon.

Let f_p(x,delta) be the entire limiting rank density of Q_p, and let
M_p(delta)=max_x f_p(x,delta). Then

    4M_1(delta)+M_2(delta)+7M_3(delta)+2M_4(delta)
                         <=28-epsilon/3<28.        (11)

Here is an explicit bound, including the displaced maximizing rank.
Let g be the convolution of [0,1]^3 and [0,2], and define

    g_p(x)=sum_(j=0)^(p-2) g(x-1-j)
                   -sum_(j=p)^3 g(x-1-j).

Changing the cut adds the low-only threshold boxes and removes the
high-only boxes, with the common threshold box cancelling. Thus exactly

    f_p(x,delta)=f_0(x)+integral_0^delta g_p(x-v)dv. (12)

There are three summands in g_p. Since g is the convolution of a
probability density on [0,3] with [0,2], 0<=g<=1, and |g_p|<=3.
Writing f_3 for the density of three independent unit uniforms gives
g'(x)=f_3(x)-f_3(x-2). The elementary three-piece quadratic formula
has 0<=f_3<=3/4, so |g_p'|<=9/4. Consequently

    |f_p(x,delta)-f_0(x)-delta g_p(x)|
                                      <=(9/8)delta^2.           (13)

All maximizing ranks lie inside |x-5|<1/4 for the chosen epsilon.
Indeed outside that interval f_0<=2-1/6144, so (12) gives
f_p<=2-1/6144+3epsilon. At x=5, (7) and (13) give the lower bound
2-(11/6)epsilon-(9/8)epsilon^2. The latter is larger because
1/6144=(16/3)epsilon and epsilon/2>(9/8)epsilon^2.

On |h|<=1/4, direct use of the same quadratic formula gives

    |g_p'(5+h)|<=3/4 for p=1,4,
    |g_p'(5+h)|<=7/4 for p=2,3.                    (14)

For example g_1'(5+h)=-1/2+h+h^2/2 when h<=0 and -1/2+h when
h>=0; g_2'(5+h)=-3/2+h+3h^2/2 when h<=0 and -3/2+h+h^2/2 when
h>=0. The p=4,3 formulas respectively replace h by -h. These expressions
prove (14) directly on the stated interval.

If L_p is the corresponding bound from (14), then (6),(13) imply

    M_p(-epsilon)
       <=2-epsilon d_p
          +(3/4)6^(1/3)(L_p epsilon)^(4/3)
          +(9/8)epsilon^2.                         (15)

The middle term is the maximum of -h^4/24+epsilon L_p|h| over real h.
The total weights of the outer and inner positions are six and eight.
Their weighted middle-term constant is less than 31: using
6^(1/3)<11/6, (3/4)^(1/3)<1, and (7/4)^(1/3)<5/4 gives the upper
bound 6*(33/32)+8*(385/128)=121/4<31. Hence

    sum_p n_p M_p(-epsilon)
      <=28-(4/3)epsilon+31epsilon^(4/3)+(63/4)epsilon^2.

Since epsilon^(1/3)=1/32, the saving coefficient is
35/96-(63/4)epsilon, which exceeds 1/3. This proves (11).

This explicit point is a mathematical rank-max certificate, not a
recommendation to enumerate the corresponding huge integer grid. It
still does not provide the actual chain partition needed by the finite
inflation theorem. A chain partition meeting the weighted finite gate,
or a constructive theorem giving an adequate upper bound, remains
necessary before any terminal improvement follows.
