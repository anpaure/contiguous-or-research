# Exact translated returns, nonprimitive-row periods, and signature multiplicities

2026-09-08. Independent pure-proof audit by `exact_b_induction` of the
claims transcribed in `ROTATION_PERIOD_ADVANCE_USER_CLAIMS_20260908.md`.
No mathematical computation was run for this note. The translated-return
equivalence, exact period formula, symmetry-loss divisor, and state/root
multiplicity all pass. Finite partition-census outputs and the separate
construction-specific overhead barrier are not computed here.

## 1. Precise conventions and inherited facts

Let A be a labelled rank-r binary word on n=2r+1 physical sites. The
physical PBBS step f complements every bit except the distinguished
unmatched zero. Write rho^K for positive spatial rotation: a particle
originally at physical edge x appears at x+K after this rotation.
The recorded-bit convention is consequently

    (rho^K w)_i = w_(i-K).

The original owner-cycle map is g=f^2. At successive peak-pruning depths
write

    n_0=n > n_1 > ... > n_h=1,
    p_s=n_(s+1),
    d_s=least cyclic period of original incoming-gap row Z_s,
    e_s=p_s/d_s.

A zero row has least period1. The last row, of length p_(h-1)=1, also
has d_(h-1)=e_(h-1)=1 regardless of its mass. No row with index -1
is used below.

The exact dynamical input is Theorem14.1 and equation(14.4) in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, beginning at lines1175
and1224. Each physical update moves exactly one persistently labelled
equality particle forward by one edge. The particles do not overtake.
Their recorded-bit word receives exactly one child PBBS update, at the
same time parameter T; it is not accelerated or divided by a
circumference.

The invariant incoming-gap coordinates are established in §§1–2 of
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`:

    L_i(t)=2 Z_i+1+epsilon_i(t),
    epsilon_i(t)=1{recorded bits at i-1 and i differ}.

Every Z_i is fixed at its persistent label. These finite facts, including
the one-particle terminal case, were also fully checked in
`PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`,
read again for the present audit.

## 2. One-level translated-return equivalence

Consider a parent of length n with p equality particles and invariant
row Z of least cyclic period d. Let B be its original recorded child
word on the p persistent particle labels. Choose ordered integer lifts
of particle positions, with

    x_(i+p)(0)=x_i(0)+n,

and lift every actual move positively. For integers T>=0 and K, the
following are equivalent:

1. f^T(A)=rho^K(A).
2. There exists an integer m satisfying

       T=n m+p K,    d divides m,
       f_child^T(B)=rho^(-m)(B).                         (2.1)

Necessity includes the sign of the child translation. At a physical
translated return, the equality-edge set is the original set translated
by K. An order-preserving correspondence between the periodically
extended particle sets has one common integer shift m, so

    x_i(T)=x_(i+m)(0)+K                                  (2.2)

for every i. Exactly one particle advances one edge at each step.
Summing displacements over any p consecutive persistent labels gives

    T=sum_i[x_i(T)-x_i(0)]=n m+p K.                     (2.3)

Here sum_i[x_(i+m)(0)-x_i(0)]=n m, including negative m: increasing
m by one increases this sum by n, and it is zero at m=0.

The bit recorded at particle i at time T is the old bit at label i+m.
Under the stated rotation convention this is rho^(-m)(B), not
rho^(+m)(B). The incoming gap is likewise the original incoming gap at
i+m. Row invariance then gives Z_i=Z_(i+m), which is equivalent to
d dividing m.

For sufficiency, assume (2.1). The translated child bits imply
epsilon_i(T)=epsilon_(i+m)(0). Row symmetry implies Z_i=Z_(i+m).
Therefore the exact gap formula gives

    L_i(T)=L_(i+m)(0)

for all persistent labels. Hence all differences

    x_i(T)-x_(i+m)(0)

are one common integer c. The displacement identity gives
T=n m+p c; comparing with (2.1) forces c=K. Thus particle positions
and their recorded bits are exactly those of rho^K(A).

These data determine the entire parent word: at least one equality
edge exists; its recorded common bit fixes its endpoints; moving
around the physical circle keeps a bit at an equality edge and flips
it at an unequal edge. The parent therefore equals rho^K(A).

For p=1, the sole recorded word is zero, d=1, its incoming gap is n,
and its one particle moves each step. The same proof reduces directly
to T=n m+K. No two-distinct-neighbors argument is applied at this
terminal case.

The equivalence is unchanged by replacing K with K+n: m changes to
m-p, which preserves its row-symmetry condition and child rotation
modulo p. Thus it is well-defined for a physical rotation class.

## 3. Iterate the equivalence without a primitivity assumption

Define

    sigma_0=0,
    sigma_j=sum_(s=0)^(j-1) 1/(n_s n_(s+1)),  1<=j<=h.

At level s let K_s be the desired translation. Equation(2.1) gives

    K_(s+1)=(n_(s+1) K_s-T)/n_s,
    d_s divides K_(s+1).                                (3.1)

The division condition includes integrality. Iterating the recurrence
from K_0=K gives

    K_j=n_j*(K/n_0-T sigma_j).                          (3.2)

The condition d_(j-1)|K_j is exactly

    (n_j/d_(j-1))*(K/n_0-T sigma_j) is an integer.       (3.3)

Necessity follows by successive applications of Section2. For
sufficiency, if every (3.3) holds, each K_j is an integer because
n_j/d_(j-1) is an integer and K_j is d_(j-1) times the integer in
(3.3). The one-site bottom is unchanged by every integer translation
and every update time. Apply the one-level sufficiency backward from
that bottom, using (3.1) and the row-symmetry divisibilities. This
establishes the original translated return.

Therefore the exact user statement holds:

    f^T(A)=rho^K(A)
      iff e_(j-1)*(K/n_0-T sigma_j) is integral
          for every j=1,...,h.                         (3.4)

No primitive-row hypothesis or independence assertion occurs in this
argument. A nonprimitive or zero row is handled by its actual least
period d_s. Persistent labels are never reset at a reached root.

## 4. The exact labelled f and f² period

Set K=0 in (3.4). For a rational number x in reduced form, a positive
integer T satisfies Tx integral exactly when den(x) divides T. Thus
the least physical f-return time is

    v(A)=lcm_(j=1)^h den(e_(j-1)*sigma_j).               (4.1)

All n_s are odd. Each sigma_j therefore has odd denominator, and
multiplication by the integer e_(j-1) cannot introduce an even factor.
The lcm in (4.1) is odd. Squaring a cyclic permutation of odd length
preserves that length, so (4.1) is also the exact g=f² period.

If r=0, the state has n=1 and h=0; taking the empty lcm to be1 gives
the correct one-site period. For r>0 the final j=h term is present;
there is no omitted terminal congruence.

As a consistency check, if every row is primitive then all e_s=1.
Clearing every sigma_j is equivalent to clearing their consecutive
differences 1/(n_(j-1)n_j). The exact period then becomes

    lcm_(s=0)^(h-1) n_s n_(s+1),

agreeing with the independently proved primitive-row upper/lower
period result in
`PBBS_FULL_PROFILE_UPPER_PERIOD_AND_PRIMITIVE_EQUALITY_AUDIT_20260908.md`.

## 5. The exact symmetry-loss divisor

For 1<=L<=h put

    M_L=lcm_(s=0)^(L-1)(n_s n_(s+1)),
    E_L=lcm_(s=0)^(L-1)e_s.

The exact period satisfies v e_(j-1) sigma_j integral for j<=L.
Since E_L is a multiple of every such e_(j-1), all v E_L sigma_j
are integers. Subtracting consecutive values, including sigma_0=0,
proves

    v E_L/(n_(j-1)n_j) is an integer for every j<=L.

Hence

    M_L divides v E_L,
    M_L/gcd(M_L,E_L) divides v,
    v >= M_L/E_L.                                      (5.1)

The middle assertion is the exact integer divisor; the final real
lower bound is weaker. This does not replace E_L by a product without
explanation, nor infer independent physical returns at nonprimitive
intermediate levels. The translated-return conditions are what permit
the descent in that case.

## 6. Original root arrays and least-period counting

Write the peak counts as

    m_s=(n_s-n_(s+1))/2,   s=0,...,h-1,
    m_h=0.

They form a positive nonincreasing partition of r. Conversely such a
partition recovers a feasible profile by

    n_s=1+2 sum_(j>=s)m_j,
    ell_s=m_s-m_(s+1)>=0.

The original inverse-pruning theorem in the structural source cited in
Section1 is a rooted bijection. Given the deeper rooted core and the
entire incoming-gap vector, the core bits and gap lengths reconstruct
the parent cyclic word and its specified root uniquely. Every weak
composition of ell_s into p_s=n_(s+1) parts is admissible. Successively
reconstructing from the one-site bottom therefore identifies the
normalized Dyck roots of a fixed profile with the Cartesian product
of these original row sets. In particular, the row count does not
carry an unaccounted rotation quotient.

For d|p, a p-entry row fixed by a shift of d is a block of length d
repeated p/d times. Its total mass can be ell only when p/d divides
ell, and in that case its block is an arbitrary weak composition of
ell/(p/d) into d parts. The exact dividing-period count is consequently

    F_(p,ell)(d)=binom(ell/(p/d)+d-1,d-1)
                  if p/d divides ell, and0 otherwise.

Every row fixed by that shift has one least period a dividing d.
Subtracting the already counted proper divisors gives

    chi_(p,ell)(d)=F_(p,ell)(d)
                   -sum_(a|d,a<d)chi_(p,ell)(a).        (6.1)

This treats ell=0 correctly: there is one zero row, of least period1,
and no other least-period possibilities. It also treats p=1 correctly:
its unique row, whatever its mass, has least period1.

For a fixed profile and least-period signature (d_0,...,d_(h-1)), the
number of normalized roots is exactly

    a=product_s chi_(p_s,ell_s)(d_s).                    (6.2)

Each such root has n distinct physical rotations. Indeed a rank-r
word on n=2r+1 sites cannot have a nontrivial rotational stabilizer:
its rotation-orbit block size would divide both n and the number r
of one-bits, whereas gcd(n,r)=1. Equivalently, each physical word has
one distinguished unmatched zero, and rotating that root to the
reference site gives one normalized Dyck root and one root position.
Thus the exact physical-state multiplicity is n*a.

The signature is invariant along f and g orbits: the profile is
invariant, each original gap vector is invariant on persistent labels,
and rotating its labels when recording a canonical current root does
not change its least cyclic period. Formula(4.1) gives the same period
v to every state in this signature. These states are therefore a
disjoint union of full v-cycles, so

    n*a/v is an integer and is the exact number of cycles. (6.3)

This proves the claimed quotient rather than merely assuming a
numerically observed divisibility.

## 7. The stated n=17 mixed-symmetry example

For profile (17,9,7,5,3,1), the peak partition is (4,1,1,1,1)
and row masses are (3,0,0,0,1). The top row has nine slots and mass3,
so there are binom(11,8)=165 rows. Exactly three have least period3:
their repeated three-entry block has mass1. The remaining162 have
least period9. All deeper rows have least period1.

The sigma values are

    sigma_1=1/153,
    sigma_2=8/357,
    sigma_3=13/255,
    sigma_4=2/17,
    sigma_5=23/51.

The deeper repetition factors are 7,5,3,1, so their denominator lcm
is51. The primitive top row has e_0=1 and supplies denominator153;
the period-three top row has e_0=3 and supplies denominator51. The
two physical periods are therefore exactly153 and51, respectively.

Their cycle counts are

    17*162/153=18,
    17*3/51=1.

Hence 18*153+51=17*165 as claimed. These are direct symbolic integer
identities, not results of a separate computational census.

## 8. Consequence for the exact construction census, and its boundary

For the unchanged height-adaptive compiler, each cycle contributes its
period to the base W(n) and exactly2h-1 collar letters. Summing the
cycle count(6.3) gives the exact finite expression

    C_n=n sum_(m partition r)(2h(m)-1)
                 sum_d [product_s chi_s(d_s)]/v(m,d).    (8.1)

There is no missing root-rotation or row-rotation correction in (8.1).
It counts the unchanged compiler rather than claiming that its output
is an optimal word. Actual evaluation of the reported odd dimensions
through101 is a separate bounded computation; no such output is
asserted to have been replayed in this pure-proof note.

Likewise, this exact period formula does not itself give a capped-bank
fusion, preserve longer witnesses through new seams, or settle
nu(k)=B(k). It supplies exact periods and multiplicities for the
specified original PBBS construction.
