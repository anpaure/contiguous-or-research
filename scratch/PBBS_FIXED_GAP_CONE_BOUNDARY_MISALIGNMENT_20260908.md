# A fixed-gap obstruction to the common-C-boundary cone transfer

2026-09-08. Pure proof; no computation. This is a theorem about one
specific proposed interface from original-index cones to physical births.
It does not disprove eligible-label divergence or occupied-support decay.
Independent cover-selectors proof audit passed; scope was checked separately
from any eligible-label divergence claim.

## 1. The natural boundary and a lower-row mismatch

Use the actual F0 incidence law, the notation, safe profile domain, and
accepted finite-layer fibre of
`PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md`. Fix S>=4. Condition the
base on its safe zero triangle F_S=0. In its original depth-S trajectory,
let t_0=0 and let t_j be the endpoint of the j-th consecutive C clock,
for j=1,2,3,4. These are the first four C boundaries in the base word
C^S T, so each t_j is even and t_4<2T(D)+1<=2H+1.

For every row s>=3 below S, the base triangle forces the coordinates
0,-1,-2,-3 to vanish. Repeatedly lifting C->C through these rows gives

    lambda_3(t_j)=-j,  j=0,1,2,3,4.

At row two, the coordinates 0,-1,-2 also vanish. Hence

    lambda_2(t_j)=-j,  j=0,1,2,3.

Now impose the free-coordinate value Z_(2,-3)=1. At time t_3, the selected
level-three particle is -3 and the selected level-two physical site is
-3. Its incoming separation from particle -4 is 2*1+1=3. The first
later selection of particle -4 is precisely t_4. The exact particle
position formula says that the predecessor's first selection omits
site ell-2z-1 when the initial selected site is ell and the incoming
gap is z. Consequently

    lambda_2(t_4)=-3-2*1-1=-6.                       (1)

All indices above are persistent original indices. The safe profile
domain excludes the relevant spatial wraps, so the displayed small
integer indices represent distinct residues.

The original-index cone Q_S(4) asks in row one for zeros at -4,-5.
It does not ask for the coordinate -6. It asks in row two for zeros
at -4,-5,-6, leaving the perturbation coordinate -3 free. Thus Q_S(4)
is compatible with both

    Z_(2,-3)=1,    Z_(1,-6)=M,                       (2)

for any fixed positive integer M. At the physical birth d=t_4/2, (1)
makes the canonical incoming gap of its reached level-one root equal
to M, rather than one of the zeros imposed by Q_S(4).

## 2. The mismatch can reject the virtual lifetime test

At d=t_4/2 consider the virtual top-gap-zero birth used in the exact
eligible-label definition k0. Suppose its virtual lifetime were at most
H. The safe profile domain then makes its clock partition valid through
the first two reduced levels.

Writing F for its reached level-one root, whose height is h-1, the
top-gap-zero partition gives

    T_virtual = C(F) + T(Psi F).

The reached height in the second summand is h-1. Since F's incoming
gap is M, its C partition consists of one deeper C followed by 2M
deeper T clocks. Every such deeper root has height h-2. Thus

    C(F) >= 1 + 2M(h-2) + M,
    T_virtual >= (2M+1)h-3M.                         (3)

This argument only invokes the short-clock partition after supposing
that the virtual cutoff passes. It does not apply a no-wrap identity
to an uncontrolled long return. Equivalently one can realize top gap
zero in a compatible top fibre and apply the exact predecessor-count
criterion there; all deeper data remain fixed.

For any fixed epsilon>0 choose M with (2M+1)epsilon>c. On h>=epsilon
sqrt(r), inequality (3) exceeds H=floor(c sqrt(r)) for sufficiently
large r. Therefore this candidate has N_d(H)<2 and is NOT eligible
for k0, regardless of the sampled offset or the actual top-row gap.

## 3. The obstruction has positive actual-incidence probability

The imposed entries in (2) are free, distinct, and outside all zeros
required by the base triangle and Q_S(4). The accepted stable
finite-coordinate limit gives

    Pr(Z_(2,-3)=1) -> (15/16)(1/16)=15/256,
    Pr(Z_(1,-6)=M) -> (8/9)(1/9)^M.

The limiting cone probability is

    u_(4,S) = (1/5)[(S+2)/(S+1)]^4.

The product limit is stable relative to the full profile and exposed
deeper environment. Consequently, writing E_(r,S,M) for the safe base
zero triangle, Q_S(4), and (2),

    Pr_inc(E_(r,S,M) intersect {h>=epsilon sqrt(r)})
      = [15/(32*9^(M+1))] u_(4,S)
          Pr_inc(h>=epsilon sqrt(r)) + o(1).         (4)

For fixed S, the safe/base-triangle exceptional mass is o(1).
The accepted short-incidence small-height estimate implies

    Pr_inc(h<epsilon sqrt(r))
        <= C_c exp(-b_c/epsilon^2).

Choose epsilon sufficiently small that this upper bound is below 1/2,
and then choose the fixed M in Section 2. Formula (4) gives a strictly
positive lower limiting probability of a raw cone whose natural fourth
common deeper C-boundary birth fails k0's virtual cutoff. Taking the
iterated S limit leaves the explicit lower bound

    3/[64*9^(M+1)] > 0.

Only fixed gap values are used. The already proved all-original-gap
logarithmic bound can also be intersected without changing this positive
lower limit, since its incidence exception is o(1).
Likewise the accepted initial-P estimate permits intersecting with
p0>m_r for any deterministic m_r=o(r^(1/4)); its incidence exception
is o(1). Thus a long initial P-run does not repair this particular map.

This does not say that all physical births associated with the same
cone are bad, that a suitable subsequence of cones cannot work, or that
k0 fails to diverge. It shows that the accepted recurrent original-array
cones cannot be transferred deterministically using their common deeper
C boundaries. A successful proof must control the actual lower-level
cocycle and the resulting lifetime and overlap tests statistically, or
provide a different interface.
